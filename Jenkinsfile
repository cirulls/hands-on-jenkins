pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building'
      }
    }

    stage('123Test') {
      parallel {
        stage('123') {
          steps {
            'echo '123'; exit 1'
          }
        }

        stage('234') {
          steps {
            echo '234'
          }
        }

      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying'
      }
    }

  }
}
