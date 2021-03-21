#! /bin/bash

scp -i ~/.ssh/id_rsa docker-compose.yaml jenkins@35.227.157.65:/home/jenkins/docker-compose.yaml
ssh -i ~/.ssh/id_rsa jenkins@35.227.157.65 << EOF
docker stack deploy --compose-file /home/jenkins/docker-compose.yaml myproject2 << EOF