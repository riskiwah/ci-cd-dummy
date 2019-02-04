pipeline {
    agent any
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
    }
}