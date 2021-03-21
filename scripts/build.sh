#! /bin/bash

sudo chmod 666 /var/run/docker.sock
docker-compose down --rmi all
docker-compose build
sudo docker login -u nubimari -p password123
sudo docker-compose push