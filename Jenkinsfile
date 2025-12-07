pipeline {
    agent { label 'ubuntu3' }

    stages {
        stage('Clone Main Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/MUGHEESULHASSAN/testing-_mern_web_app_with_jenkins_pipeline.git'
            }
        }

        stage('Build & Run Main Containers') {
            steps {
                sh 'sudo docker compose down || true'
                sh 'sudo docker compose up -d --build'
            }
        }

        stage('Verify Running Containers') {
            steps {
                sh 'sudo docker ps'
            }
        }

        stage('Show Logs') {
            steps {
                sh 'sudo docker compose logs --tail=50'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                // Clone Selenium test repository
                sh 'git clone https://github.com/MUGHEESULHASSAN/test_cases_assignment_3.git '
                sh 'sleep 20'
                
                // Navigate into test repo
                dir('test_cases_assignment_3') {
                    // Build Docker container for Selenium tests
                    sh 'sudo docker build -t selenium-tests .'

                    // Run container and connect to main app network
                    sh 'sudo docker run selenium-tests '
                }
            }
        }
    }

    post {
        success {
            echo "✅ CI Build Completed Successfully!"
        }
        failure {
            echo "❌ Build Failed. Check logs."
        }
    }
}
