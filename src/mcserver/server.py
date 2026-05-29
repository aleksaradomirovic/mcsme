# Copyright (C) 2026  Aleksa Radomirovic
# SPDX-License-Identifier: Apache-2.0

import contextlib
import os
import pathlib
import shutil
import tarfile
import tempfile

from .modules import fabric

from .logging import log

class Server():
    def __init__(self, directory=None):
        if directory is None:
            self.temp_dir = tempfile.TemporaryDirectory(delete=True)
            directory = self.temp_dir.name

        self.directory = pathlib.Path(directory)
        self.server_jar = self.directory / "server.jar"
        self.java_args = []

        log.debug(f"creating server at {self.directory}")

    def setup(self):
        eula_file = self.directory / "eula.txt"

        if not eula_file.exists():
            with open(eula_file, "w") as f:
                f.write("eula=true")

    @contextlib.contextmanager
    def run(self):
        self.setup()

        pid = os.fork()
        if pid == 0:
            os.chdir(self.directory)
            os.execvp("java", [ "java", "-jar", self.server_jar ] + self.java_args)
        else:
            try:
                yield pid
            finally:
                _, status = os.waitpid(pid, 0)
                code = os.waitstatus_to_exitcode(status)
                if code != 0:
                    raise RuntimeError(f"server process exited with error code {code}")

class FabricServer(Server):
    def __init__(self, game_version=None, loader_version=None, installer_version=None, gui=False, **kwargs):
        super().__init__(**kwargs)

        if not gui:
            self.java_args.append("--nogui")

        with fabric.get_server_jar(game_version=game_version, loader_version=loader_version, installer_version=installer_version) as fabric_jar_dl, open(self.server_jar, "wb") as server_jar_file:
            shutil.copyfileobj(fabric_jar_dl, server_jar_file)

