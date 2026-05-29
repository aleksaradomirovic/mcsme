# Copyright (C) 2026  Aleksa Radomirovic
# SPDX-License-Identifier: Apache-2.0

import logging

import mcserver

logging.basicConfig(level=logging.DEBUG)

with mcserver.fabric.get_server_jar(mcserver.fabric.get_best_version()) as jar:
    pass

