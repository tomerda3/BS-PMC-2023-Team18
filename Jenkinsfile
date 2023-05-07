pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/BS-PMC-2023/BS-PMC-2023-Team18.git']]])
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python manage.py test'
            }
        }
        stage('Build') {
            steps {
                sh 'python manage.py collectstatic --noinput'
            }
        }
        stage('Deploy') {
            steps {
                // Add your deployment steps here
            }
        }
    }
}
