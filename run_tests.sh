#!/bin/bash

echo Creating new container
docker create -ti --name rover-ninja rover_challenge:1.0
echo Running test
docker start rover-ninja
docker exec rover-ninja python -m unittest discover
echo Stopping container
docker stop rover-ninja
echo Removing old container
docker rm rover-ninja
