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
import shutil

import mcsme

def __get_modrinth_loader_id(loader):
    import mcsme.fabric
    if isinstance(loader, mcsme.fabric.FabricServerLoader):
        return "fabric"
    else:
        raise ValueError("unsupported loader type")

def retrieve_modrinth_mod(mod_id, loader, folder):
    with open(mcsme.retrieve_file(f"modrinth/project/{mod_id}/versions.json", f"https://api.modrinth.com/v2/project/{mod_id}/version"), "r") as f:
        versions = json.load(f)

    loader_str = __get_modrinth_loader_id(loader)
    game_version = loader.game_version()

    valid_versions = [ v for v in versions if (loader_str in v["loaders"]) and (game_version in v["game_versions"]) ]
    mod_version = valid_versions[0]
    mod_version_id = mod_version["id"]

    files = []
    for file in mod_version["files"]:
        file_url = file["url"]
        file_id = file["id"]
        file_name = file["filename"]
        files.append(mcsme.retrieve_file(f"modrinth/project/{mod_id}/versions/{mod_version_id}/{file_id}", file_url))

    return files
