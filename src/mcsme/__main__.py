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

import argparse
import json
import mcsme
import pathlib

parser = argparse.ArgumentParser("mcsme")
parser.add_argument("-C", "--directory", type=pathlib.Path, default=pathlib.Path.cwd(), help="specify server directory (default current)")
parser.add_argument("--init-only", action="store_true", help="only initialize server, do not run")
args = parser.parse_args()

args.directory.mkdir(exist_ok=True)
config_file = args.directory / "mcsme-config.json"

if config_file.exists():
    with open(config_file, "r") as f:
        config = json.load(f)
else:
    config = {}

config.setdefault("loader", {})
config_loader_type = config["loader"].setdefault("type", "fabric")

match(config_loader_type):
    case "fabric":
        import mcsme.fabric
        game_version = config["loader"].get("game_version", None)
        loader_version = config["loader"].get("loader_version", None)
        installer_version = config["loader"].get("installer_version", None)

        loader = mcsme.fabric.retrieve_fabric_server_loader(game_version, loader_version, installer_version)

        config["loader"]["game_version"] = loader.game_version()
        config["loader"]["loader_version"] = loader.loader_version()
        config["loader"]["installer_version"] = loader.installer_version()
    case _:
        raise ValueError(f"invalid loader type {config_loader_type}")

with open(config_file, "w") as f:
    json.dump(config, f, indent="\t")

if not args.init_only:
    server = mcsme.ServerInstance(args.directory, loader)
    server.run()
