pipeline {
    agent any
    stages{
        stage ("checkout") {
            steps {

            }
        }
        stage ("branch deploy") {
            sh 'echo $BRANCH > BRANCH_FILE'
        }
        stage ("docker build") {
            sh 'docker build -t riskiwah/cidummy .'
        }
        stage ("docker push") {
            sh 'docker push riskiwah/cidummy'
        }
    }
}