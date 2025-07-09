pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/rohan11131113/pythonapp.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-python-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 my-python-app'
            }
        }
    }
}
