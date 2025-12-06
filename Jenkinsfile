pipeline {
    agent { label 'ubuntu3' }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/MUGHEESULHASSAN/testing-_mern_web_app_with_selenium_test_cases_with_jenkins_pipeline.git'
            }
        }

        stage('Build & Run Containers') {
            steps {
                sh 'sudo docker-compose down || true'
                sh 'sudo docker-compose up -d --build'
            }
        }

        stage('Verify Running Containers') {
            steps {
                sh 'sudo docker ps'
            }
        }

        stage('Show Logs') {
            steps {
                sh 'sudo docker-compose logs --tail=50'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh 'sudo docker-compose run --rm selenium-tests'
            }
        }
    }

    post {
        always {
            echo "Archiving screenshots..."
            sh 'mkdir -p screenshots'
            sh 'sudo docker cp selenium-tests:/app/screenshots ./screenshots || true'
        }
        success {
            echo "✅ CI Build Completed Successfully!"
        }
        failure {
            echo "❌ Build Failed. Check logs."
        }
    }
}
