pipeline {
    agent any
    stages {
        try {
        stage("checkout"){
            steps{
            checkout([$class: 'GitSCM', 
            branches: [[name: '*/master']], 
            doGenerateSubmoduleConfigurations: false, 
            extensions: [[$class: 'SubmoduleOption', 
            disableSubmodules: false, 
            parentCredentials: true, 
            recursiveSubmodules: true, 
            reference: '',
            trackingSubmodules: false]],
            submoduleCfg: [], 
            url : 'https://github.com/riskiwah/cicdummy.git'])
            }
        }
        stage("start build"){
            steps{
                sh 'curl -s -X POST https://api.telegram.org/bot737736425:AAHaSlsEBMNIDy9xm8On_7ULKPb9f-PdAWo/sendMessage -d chat_id=726982393 -d text="start build"'
            }
        }
        stage("branch deploy"){
            steps{
                sh 'echo $BRANCH > BRANCH_FILE'
            }
        }
        stage("docker build"){
            steps{
                sh 'docker build -t riskiwah/cidummy .'
            }
        }
        stage("docker push"){
            steps{
                sh 'docker push riskiwah/cidummy'
            }
        }
        stage("deploy to k8s"){
            steps{
                sh 'kubectl create namespace staging'
                sh 'kubectl apply -f k8s/*'
                sh 'kubectl get po -o wide -n staging'
            }
        }
        stage("end build"){
            steps{
                sh 'curl -s -X POST https://api.telegram.org/bot737736425:AAHaSlsEBMNIDy9xm8On_7ULKPb9f-PdAWo/sendMessage -d chat_id=726982393 -d text="end build"'
            }
        }

    }catch(e){
    currentBuild.result = "FAILURE"
    throw e
    }finally {
        if(currentBuild.result == 'FAILURE'){
            sh 'curl -s -X POST https://api.telegram.org/bot737736425:AAHaSlsEBMNIDy9xm8On_7ULKPb9f-PdAWo/sendMessage -d chat_id=726982393 -d text="build failure"'
        }
    }
}
}