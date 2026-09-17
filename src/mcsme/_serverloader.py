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

import pathlib

class ServerLoader:
    def __init__(self, jar_file, game_version):
        if jar_file is None:
            raise ValueError("jar_file cannot be null")
        self.__jar_file = pathlib.Path(jar_file)

        if game_version is None:
            raise ValueError("game_version cannot be null")
        if not isinstance(game_version, str):
            raise TypeError("game_version must be of type str")
        self.__game_version = str(game_version)

    def jar_file(self) -> pathlib.Path:
        return self.__jar_file
    
    def game_version(self) -> str:
        return self.__game_version
