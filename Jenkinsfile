pipeline {
    agent any
    stages{
        stage ("checkout") {
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
            url : 'https://github.com/riskiwah/cicdummy.git']])
        }
        stage ("branch deploy") {
            sh 'echo $BRANCH > BRANCH_FILE'
        }
        // stage ("docker login") {
        //     sh 
        // }
        stage ("docker build") {
            sh 'docker build -t riskiwah/cidummy .'
        }
        stage ("docker push") {
            sh 'docker push riskiwah/cidummy'
        }
    }
}