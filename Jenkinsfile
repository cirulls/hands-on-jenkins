pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Build'
      }
    }
    stage('Test') {
      parallel {
        stage('Firefox') {
          steps {
            sh 'echo "Test on Firefox"'
          }
        }
        stage('Chrome') {
          steps {
            sh 'echo "Test on Chrome"'
          }
        }
        stage('Edge') {
          steps {
            sleep 5
			exit 1
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
