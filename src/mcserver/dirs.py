# Copyright (C) 2026  Aleksa Radomirovic
# SPDX-License-Identifier: Apache-2.0

import pathlib

import platformdirs

APP_NAME = "mcserver"

DATA_DIR  = pathlib.Path(platformdirs.user_data_dir(APP_NAME))
CACHE_DIR = pathlib.Path(platformdirs.user_cache_dir(APP_NAME))
STATE_DIR = pathlib.Path(platformdirs.user_state_dir(APP_NAME))
