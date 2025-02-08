from django.core.management.base import BaseCommand
from django.conf import settings
from helpers import download_to_local
from home.settings import STATICFILES_VENDOR_DIR

STATICFILES_DIRS = getattr(settings, "STATICFILES_VENDOR_DIR")

VENDOR_STATICFILES = {
    "flowbite.min.js": "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js",
    "flowbite.min.css": "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.css",
}


class Command(BaseCommand):
    help = 'Pull vendor files from CDN'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE(
            "Pulling vendor files from CDN..."))
        comleted_urls = []
        for filename, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIR / filename
            print(f"Downloading {filename}...")
            dl_success = download_to_local(url, out_path)
            if dl_success:
                comleted_urls.append(url)
            else:
                self.stdout.write(self.style.ERROR(
                    f"Failed to download {url}"))

        if set(comleted_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(self.style.SUCCESS(
                "All vendor files downloaded successfully"))
        else:
            self.stdout.write(self.style.ERROR(
                "Some vendor files failed to download"))
