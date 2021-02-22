pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building...'
      }
    }
    stage('Test') {
      parallel {
        stage('Test Firefox') {
          steps {
            cmd 'echo \'Testing Firefox\''
          }
        }
        stage('Test Chrome') {
          steps {
            cmd 'echo \'Testing Chrome\''
          }
        }
        stage('Test Edge') {
          steps {
            cmd 'echo \'Testing Edge\''
          }
        }
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploy'
      }
    }
  }
}
