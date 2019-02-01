pipeline {
    agent any
    stages{
        stage ("checkout"){
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
            url : ''
        }
    }
}