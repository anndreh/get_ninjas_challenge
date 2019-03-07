#!/bin/bash

echo Runing application
docker run -ti --name rover-ninja rover_challenge:1.0
echo Removing old container
docker rm rover-ninja
