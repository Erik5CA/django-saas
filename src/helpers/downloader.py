import requests
from pathlib import Path


def download_to_local(url: str, out_path: Path, parent_mkdir: bool = True):
    if not isinstance(out_path, Path):
        raise TypeError(f"{out_path} is not a Path object")

    if parent_mkdir:
        out_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        response = requests.get(url)
        response.raise_for_status()
        out_path.write_bytes(response.content)
        return True
    except requests.exceptions.HTTPError as e:
        print(f"Failed to download {url} to {out_path}: {e}")
        return False
