# Copyright (C) 2026  Aleksa Radomirovic
# SPDX-License-Identifier: Apache-2.0

import hashlib
import io
import pathlib
import time
import urllib.request

from . import dirs
from .logging import log

DOWNLOADS_DIR = dirs.CACHE_DIR / "downloads"

def download(url: str, cache=True, cache_timeout=None):
    url_encoded = url.encode("ascii")

    cache_dir = DOWNLOADS_DIR / hashlib.sha512(url_encoded).hexdigest()
    cache_dir.mkdir(parents=True, exist_ok=True)

    log.debug(f"fetching {url} ...")

    url_file_path = cache_dir / "url"
    file_path = cache_dir / "get"

    if cache:
        if url_file_path.exists():
            with open(url_file_path, "rb") as f:
                old_url_encoded = f.read()
            if url_encoded != old_url_encoded:
                cache = False
        else:
            cache = False

        if file_path.exists():
            if not cache_timeout is None:
                time_diff = time.time() - file_path.stat().st_mtime
                if time_diff > cache_timeout:
                    cache = False
        else:
            cache = False

    with open(url_file_path, "wb") as f:
        f.write(url_encoded)

    if not cache:
        urllib.request.urlretrieve(url, file_path)

    return open(file_path, "r+b")
