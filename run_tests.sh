#!/bin/bash

echo Creating new container
docker run -d --name rover-ninja rover_challenge:1.0 /bin/bash
echo Running test
docker exec rover-ninja python -m unittest discover
echo Removing old container
docker rm rover-ninja
