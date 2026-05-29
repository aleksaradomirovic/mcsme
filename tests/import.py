# Copyright (C) 2026  Aleksa Radomirovic
# SPDX-License-Identifier: Apache-2.0

import mcserver

print(f"data dir:  {mcserver.dirs.DATA_DIR }")
print(f"cache dir: {mcserver.dirs.CACHE_DIR}")
print(f"state dir: {mcserver.dirs.STATE_DIR}")
print()

print(f"downloads: {mcserver.download.DOWNLOADS_DIR}")
