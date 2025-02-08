ARG PYTHON_VERSION=3.12-slim-bullseye
FROM python:${PYTHON_VERSION}

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --upgrade pip

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    libpq-dev \
    libjpeg-dev \
    libcairo2-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt

COPY ./src /code

RUN pip install -r /tmp/requirements.txt

ARG PROJECT_NAME="home"

RUN printf "#!/bin/bash\n\" > ./paracord_runner.sh && \
    printf "RUN_PORT=\"\${PORT:-8000}\"\n\n" >> ./paracord_runner.sh && \
    printf "python manage.py migrate --no-input\n\n" >> ./paracord_runner.sh && \
    printf "gunicorn ${PROJECT_NAME}.wsgi:application --bind 0.0.0.0:\$RUN_PORT\n" >> ./paracord_runner.sh

RUN apt-get remove -y gcc && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

CMD ./paracord_runner.sh