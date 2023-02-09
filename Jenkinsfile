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
    agent{
        label 'docker-slave'
        }
//     agent {
//         docker {
//             image 'jenkins/slave:latest'
//         }
//     }
//     options {
//     buildDiscarder(logRotator(numToKeepStr:'2', artifactNumToKeepStr:'2'))
//     timestamps()
//     }
    
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t fastapi-app .'
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
