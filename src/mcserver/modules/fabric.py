# Copyright (C) 2026  Aleksa Radomirovic
# SPDX-License-Identifier: Apache-2.0

import json

from .. import download

def get_versions_json():
    with download.download("https://meta.fabricmc.net/v2/versions", cache_timeout=86400) as f:
        return json.load(f)

def game_versions(stable=True):
    versions = get_versions_json()
    return [ version["version"] for version in versions["game"] if version["stable"] ]

def loader_versions():
    versions = get_versions_json()
    return [ version["version"] for version in versions["loader"] ]

def installer_versions():
    versions = get_versions_json()
    return [ version["version"] for version in versions["installer"] ]

def get_server_jar(game_version=None, loader_version=None, installer_version=None):
    if game_version is None:
        game_version = game_versions()[0]
    if loader_version is None:
        loader_version = loader_versions()[0]
    if installer_version is None:
        installer_version = installer_versions()[0]
    
    url = f"https://meta.fabricmc.net/v2/versions/loader/{game_version}/{loader_version}/{installer_version}/server/jar"
    return download.download(url)
