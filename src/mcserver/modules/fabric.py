# Copyright (C) 2026  Aleksa Radomirovic
# SPDX-License-Identifier: Apache-2.0

import json

from .. import download

def get_versions(stable=True):
    with download.download("https://meta.fabricmc.net/v2/versions", cache_timeout=86400) as f:
        versions = json.load(f)

    game_versions =         [ version["version"] for version in versions["game"] if version["stable"] or not stable ]
    loader_versions =       [ version["version"] for version in versions["loader"] ]
    installer_versions =    [ version["version"] for version in versions["installer"] ]

    return game_versions, loader_versions, installer_versions

def get_best_version(game_version=None, loader_version=None, installer_version=None):
    if (game_version is None) or (loader_version is None) or (installer_version is None):
        game_versions, loader_versions, installer_versions = get_versions()

        if game_version is None:
            game_version = game_versions[0]
        if loader_version is None:
            loader_version = loader_versions[0]
        if installer_version is None:
            installer_version = installer_versions[0]
    
    return game_version, loader_version, installer_version

def get_server_jar(version):
    game_version, loader_version, installer_version = version

    url = f"https://meta.fabricmc.net/v2/versions/loader/{game_version}/{loader_version}/{installer_version}/server/jar"
    return download.download(url)
