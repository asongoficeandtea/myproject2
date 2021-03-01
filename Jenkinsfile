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
        stage('Build'){
            steps{
                sh ''' 
                sudo chmod 666 /var/run/docker.sock
                docker-compose down --rmi all
                docker-compose build
                sudo docker login -u nubimari -p mariam123
                sudo docker-compose push
                '''
            }
        }        
        stage('Ansible'){
            steps{
                sh '''
		whoami
                chmod 666 inventory.yaml playbook.yaml
                ansible-playbook -i inventory.yaml playbook.yaml
                cd ..
                '''
            }
        }
        stage('Deploy'){
            steps{
                sh '''
                scp -i ~/.ssh/id_rsa docker-compose.yaml alimatea7@jenkins:/home/jenkins/docker-compose.yml
                ssh -i ~/.ssh/id_rsa alimatea7@jenkins
                docker stack deploy --compose-file /home/jenkins/docker-compose.yaml myproject2
                EOF
                '''
            }
        }          
    }
}
