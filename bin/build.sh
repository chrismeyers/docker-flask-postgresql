#!/usr/bin/env bash

# Change directory to correct docker context
cd "$(dirname "$0")"
cd ..

# Build all services
docker-compose build --force-rm
