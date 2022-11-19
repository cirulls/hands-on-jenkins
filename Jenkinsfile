pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Build ...'
      }
    }

    stage('Test') {
      parallel {
        stage('Test Firefox') {
          steps {
            sh 'echo \'Test Firefox\''
          }
        }

        stage('Test Chrome') {
          steps {
            sh 'echo \'Test Chrome\''
          }
        }

        stage('Test Edge') {
          steps {
            sh 'echo \'Test Edge\''
            sh 'exit 1'
          }
        }

      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploy ...'
      }
    }

  }
}
