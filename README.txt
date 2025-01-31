Minecraft Server Management Engine (MCSME)
==========================================

Currently, this is just a simple script to run minecraft servers and quickly
move server files from a /tmp filesystem to and from a server directory.

Usage:

./run_server [-p/--port HOST_PORT] SERVER_NAME

SERVER_NAME corresponds to the name of the folder in the server directory you
want to run.

HOST_PORT is in case you want to expose the server on a different port than
minecraft's default (25565).

Before you can run server, you should build the docker image in ./docker, by
running:

./docker.sh

Which will build the (very slim) Debian 13-based docker image in which the
server will be run.

Required tools to run:

rsync, docker

On Debian/Ubuntu, these can be obtained via the packages:

rsync, docker.io

The user running the script should be a member of the docker usergroup on their
system. Running any of these scripts in sudo mode is STRONGLY DISCOURAGED.
