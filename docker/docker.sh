#!/bin/bash

docker image build --build-arg UID=$(id -u) --tag minecraft .
