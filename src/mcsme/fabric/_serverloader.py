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

import mcsme

class FabricServerLoader(mcsme.ServerLoader):
    def __init__(self, jar_file, game_version, loader_version, installer_version):
        super().__init__(jar_file, game_version)

        if loader_version is None:
            raise ValueError("loader_version cannot be null")
        if not isinstance(loader_version, str):
            raise TypeError("loader_version must be of type str")
        self.__loader_version = str(loader_version)

        if installer_version is None:
            raise ValueError("installer_version cannot be null")
        if not isinstance(installer_version, str):
            raise TypeError("installer_version must be of type str")
        self.__installer_version = str(installer_version)

    def loader_version(self) -> str:
        return self.__loader_version

    def installer_version(self) -> str:
        return self.__installer_version
