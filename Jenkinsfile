#!groovy
//Run docker build
properties([disableConcurrentBuilds()])

pipeline {
    agent{
        label 'main'
    }
    options {
        buildDiscarder(logRotator(numToKeepStr:'4', artifactNumToKeepStr:'4'))
        timestamps()
    }
    stages {
        stage("create docker image"){
            steps{
                echo "========== start building image =========="
                dir (''){
                    sh 'docker build . '
                }
            }
        }
    } 
}
