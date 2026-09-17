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

import javaproperties
import pathlib
import subprocess
import typing

from ._serverloader import *

class ServerInstance:
    def __init__(self, directory, loader):
        if directory is None:
            raise ValueError("directory cannot be null")
        self.__directory = pathlib.Path(directory)

        if loader is None:
            raise ValueError("loader cannot be null")
        if not isinstance(loader, ServerLoader):
            raise TypeError("loader must be of type mcsme.ServerLoader")
        self.__loader = loader

    def directory(self) -> pathlib.Path:
        return self.__directory

    def loader(self) -> ServerLoader:
        return self.__loader

    def run(self):
        with open(self.directory() / "eula.txt", "w") as f:
            f.write("eula=true")

        subprocess.run([ "java", "-jar", self.loader().jar_file().absolute(), "--nogui" ], check=True, cwd=self.directory().absolute())
