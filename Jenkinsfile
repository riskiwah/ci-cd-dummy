pipeline {
    agent any
    // try {
    stages {
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
                sh 'curl -s -X POST https://api.telegram.org/bot<token>/sendMessage -d chat_id=<id> -d text="start build"'
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
        stage("analyze image"){
            steps{
                sh 'echo "docker.io/riskiwah/cidummy:latest `pwd`/Dockerfile" > anchore_images'
                anchore name: 'anchore_images'
            }
        }
        // stage("docker push"){
        //     steps{
        //         sh 'docker push riskiwah/cidummy'
        //     }
        // }
        // stage("deploy to k8s"){
        //     steps{
        //         sh 'kubectl apply -f k8s/*'
        //         sh 'kubectl get po -o wide -n staging'
        //     }
        // }
        // stage("end build"){
        //     steps{
        //         sh 'curl -s -X POST https://api.telegram.org/bot<token>/sendMessage -d chat_id=<id> -d text="end build"'
        //     }
        // }

    }
}
