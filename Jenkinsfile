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
                    pwd
                    ansible-playbook -i inventory.yaml playbook.yaml
                    '''
                }
            }
            stage('Deploy'){
                steps{
                    sh ''' ssh -i ~/.ssh/jenkins_agent_key manager-vm << EOF
                    sudo rm -rf myproject2
                    git clone https://github.com/asongoficeandtea/myproject2.git
                    cd myproject2
                    docker stack deploy --compose-file docker-compose.yaml myproject2
                    EOF  '''
                }
            }
        }
    }
