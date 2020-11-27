pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        echo 'building'
      }
    }

    stage('Test FF') {
      parallel {
        stage('Test FF') {
          steps {
            sh 'echo "test ff"'
          }
        }

        stage('Test Chrome') {
          steps {
            sh 'echo Chrome'
          }
        }

        stage('Test Edge') {
          steps {
            sh 'echo Edge'
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