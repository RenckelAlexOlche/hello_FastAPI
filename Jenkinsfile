// #!groovy
// //Run docker build
// properties([disableConcurrentBuilds()])

// pipeline {
//     agent{
//         label 'docker-slave'
//         }   
//     options {
//         buildDiscarder(logRotator(numToKeepStr:'4', artifactNumToKeepStr:'4'))
//         timestamps()
//     }
//     stages {
//         stage("create docker image"){
//             steps{
//                 echo "========== start building image =========="
//                 dir (''){
//                     sh 'docker build . '
//                 }
//             }
//         }
//     } 
// }

pipeline {
    agent any
       
    environment {
        DOCKERHUB=credentials('dockerhub')
    }
//     agent{
//         label 'docker-slave'
//         }
//     agent {
//         docker {
//             image 'jenkins/slave'
//         }
//     }
//     options {
//     buildDiscarder(logRotator(numToKeepStr:'2', artifactNumToKeepStr:'2'))
//     timestamps()
//     }
    
    stages {
        stage('Build image') {
            steps {
                sh 'docker build -t fastapi-app .'
            }
        }
           
    stages {
        stage('Push image to docker hub') {
            steps {            
                sh 'docker tag fastapi-app:latest renckel/hello-fastapi:latest'
                sh 'echo $DOCKERHUB_PSW | docker login -u $DOCKERHUB_USR --password-stdin'
                
                sh 'docker push renckel/hello-fastapi:latest'
            }
        }
           
        
//         stage('Test') {
//             steps {
//                 sh 'docker run --rm fastapi-app pytest'
//             }
//         }
        
//         stage('Deploy') {
//             steps {
//                 sh 'docker stop fastapi-app || true'
//                 sh 'docker rm fastapi-app || true'
//                 sh 'docker run -d --name fastapi-app -p 80:80 fastapi-app'
//             }
//         }
    }
}
