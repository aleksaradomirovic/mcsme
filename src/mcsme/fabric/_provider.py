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

import json

import mcsme
from ._serverloader import *

def __retrieve_latest_versions():
    with open(mcsme.retrieve_file("fabric/versions.json", "https://meta.fabricmc.net/v2/versions"), "r") as f:
        versions = json.load(f)

    return (
        [ v for v in versions["game"] if v["stable"] ][0]["version"],
        [ v for v in versions["loader"] if v["stable"] ][0]["version"],
        [ v for v in versions["installer"] if v["stable"] ][0]["version"]
    )

def retrieve_fabric_server_loader(game_version=None, loader_version=None, installer_version=None) -> FabricServerLoader:
    latest = __retrieve_latest_versions()

    if game_version is None:
        game_version = latest[0]
    if loader_version is None:
        loader_version = latest[1]
    if installer_version is None:
        installer_version = latest[2]

    jar_file = mcsme.retrieve_file(
        f"fabric/servers/{game_version}-{loader_version}-{installer_version}.jar",
        f"https://meta.fabricmc.net/v2/versions/loader/{game_version}/{loader_version}/{installer_version}/server/jar"
    )

    return FabricServerLoader(jar_file, game_version, loader_version, installer_version)
