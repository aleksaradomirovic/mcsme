# Copyright (C) 2026  Aleksa Radomirovic
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import email.utils
import os
import pathlib
import platformdirs
import shutil
import time
import urllib.request

__CACHE_ROOT = platformdirs.user_cache_path(appname="mcsme", ensure_exists=True)
__CACHE_EXPIRE_TIMEOUT = 3000

def retrieve_file(key, url) -> pathlib.Path:
    request_time = time.time()

    key_path = __CACHE_ROOT / key
    if not key_path.is_relative_to(__CACHE_ROOT):
        raise ValueError("illegal key name")

    key_path.parent.mkdir(parents=True, exist_ok=True)

    file_time = None
    if key_path.exists():
        file_time = key_path.stat().st_mtime

        if request_time < file_time + __CACHE_EXPIRE_TIMEOUT:
            return key_path

    request = urllib.request.Request(
        url,
        headers={
            **( { "If-Modified-Since": email.utils.formatdate(file_time, usegmt=True) } if not file_time is None else {} )
        }
    )

    try:
        with urllib.request.urlopen(request) as response:
            with open(key_path, "wb") as f:
                shutil.copyfileobj(response, f)
    except urllib.request.HTTPError as err:
        match err.code:
            case 304:
                pass
            case _:
                raise

    os.utime(key_path, ( request_time - 1, request_time - 1 ))
    return key_path
