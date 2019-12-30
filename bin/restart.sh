#!/usr/bin/env bash

# Change directory to correct docker context
cd "$(dirname "$0")"
cd ..

# Stop all containers
docker-compose down

# Bring up containers in the background
docker-compose up -d
