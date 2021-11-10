pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building.....'
      }
    }

    stage('Testing Firefox') {
      parallel {
        stage('Testing Firefox') {
          steps {
            sh 'echo \'Testing Firefox\''
          }
        }

        stage('Testing Chrome') {
          steps {
            sh 'echo \'Tesing Chrome\''
          }
        }

        stage('Testing Edge') {
          steps {
            sh 'echo \'Testing Edge\''
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