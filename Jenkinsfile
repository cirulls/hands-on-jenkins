pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building...'
      }
    }

    stage('Test Firefox') {
      parallel {
        stage('Test Firefox') {
          steps {
            sh 'echo \'Testing Firefox\''
          }
        }

        stage('Testing Chrome') {
          steps {
            sh 'echo \'Testing Chrome\';exit 1'
          }
        }

        stage('Test Edge') {
          steps {
            sh 'echo \'Testing Edge\''
          }
        }

      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying..'
      }
    }

  }
}
