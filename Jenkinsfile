pipeline {
  agent { docker { image 'python:3.7.5'  }  }
  stages {
    stage('build') {
      steps {
        sh 'echo 123'
        sh 'python --version'
      }
    }
  }
}
