# Copyright (C) 2026  Aleksa Radomirovic
# SPDX-License-Identifier: Apache-2.0

import logging

import mcserver

logging.basicConfig(level=logging.DEBUG)

# print(mcserver.fabric.game_versions())
# print(mcserver.fabric.loader_versions())
# print(mcserver.fabric.installer_versions())

with mcserver.fabric.get_server_jar() as jar:
    pass

