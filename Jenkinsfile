pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building'
      }
    }
    stage('Test') {
      parallel {
        stage('Firefox testing') {
          steps {
            sh 'echo "testing on firefox"'
          }
        }
        stage('Chrome testing') {
          steps {
            sh 'echo \'test on chrome\'; exit 1'
          }
        }
      }
    }
    stage('deploy') {
      steps {
        sh 'echo \'going to deployment\''
      }
    }
  }
}
