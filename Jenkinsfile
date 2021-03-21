pipeline{
        agent any
        stages{
            stage('Test'){
                steps{
                    sh '''
                    cd scripts
                    sudo chmod +x ./test.sh
                    ./test.sh
                    '''
                }
            }
        stage('Ansible'){
            steps{
                sh '''
                cd scripts
                sudo chmod +x ./config.sh
                ./config.sh
                '''
            }
        }
        stage('Build'){
            steps{
                sh ''' 
                cd scripts
                sudo chmod +x ./build.sh
                ./build.sh
                '''
            }
        }
        stage('Deploy'){
            steps{
                sh '''
                cd scripts
                sudo chmod +x ./deploy.sh
                ./deploy.sh
                '''
            }
        }          
    }
}