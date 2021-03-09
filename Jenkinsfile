pipeline{
        agent any
        stages{
            stage('Testing'){
                steps{
                    sh '''
                    cd service2
                    pip3 install -r requirements.txt
                    python3 -m pytest --cov=app
                    cd ..
                    cd service3
                    pip3 install -r requirements.txt
                    python3 -m pytest --cov=app
                    cd ..
                    cd service4
                    pip3 install -r requirements.txt
                    python3 -m pytest --cov=app
                    cd ..
                    '''
                }
            }
        stage('Ansible'){
            steps{
                sh ''' 
                cd ansible
                ansible_ssh_extra_args='-o StrictHostKeyChecking=no'
                ansible-playbook -i inventory.yaml playbook.yaml
                '''
            }
        }
        stage('Build'){
            steps{
                sh ''' 
                sudo chmod 666 /var/run/docker.sock
                docker-compose down --rmi all
                docker-compose build
                sudo docker login -u nubimari -p password123
                sudo docker-compose push
                '''
            }
        }
        stage('Deploy'){
            steps{
                sh '''
                scp -i ~/.ssh/id_rsa docker-compose.yaml jenkins@35.227.157.65:/home/jenkins/docker-compose.yaml
                ssh -i ~/.ssh/id_rsa jenkins@35.227.157.65 << EOF
                docker stack deploy --compose-file /home/jenkins/docker-compose.yaml myproject2 << EOF
                '''
            }
        }          
    }
}