pipeline {
    agent any 
    stages{
        stage('Test'){
            steps{
                sh ''' sudo chmod 666 ./scripts/test.sh
                ./scripts/test.sh '''
            }
        }                 
    }
}
