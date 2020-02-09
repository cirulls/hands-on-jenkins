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
            bat 'echo "Test Firefox"'
          }
        }

        stage('Test Chrome') {
          steps {
            bat 'echo \'Testing Chrome\''
          }
        }

        stage('Test Edge') {
          steps {
            bat 'echo \'Testing Edge\''
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