pipeline{
        agent any
        stages{
            stage('Testing'){
                steps{
                    sh '''
                    cd service1 
                    pip3 install -r requirements.txt
                    python3 -m pytest --cov=app
                    cd ..
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
            
        }
}
