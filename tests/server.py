# Copyright (C) 2026  Aleksa Radomirovic
# SPDX-License-Identifier: Apache-2.0

import logging
import tempfile

import mcserver

logging.basicConfig(level=logging.DEBUG)

server = mcserver.server.FabricServer()

with server.run() as instance:
    pass
