// Jenkinsfile (Declarative Pipeline for Python CI)

pipeline {
    agent {
        // Use a specific Docker image for consistency
        docker {
            image 'python:3.11-slim' 
        }
    }
    
    environment {
        VENV_NAME = 'venv' 
    }

    stages {
        stage('Setup and Install') { // Combined the steps into one stage
            steps {
                echo '1. Setting up virtual environment and installing dependencies...'
                
                // --- Single Multi-Line Shell Block for Reliability ---
                sh '''
                    # 1. Create venv
                    python -m venv ${VENV_NAME}
                    
                    # 2. Activate venv and install requirements (The 'source' command is essential here)
                    source ${VENV_NAME}/bin/activate
                    
                    # 3. Use pip inside the activated environment
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Code Quality (Lint)') {
            steps {
                echo '2. Running Flake8 Linter for code style checks...'
                sh '''
                    source ${VENV_NAME}/bin/activate
                    flake8 --exclude=${VENV_NAME} . || true
                '''
            }
        }

        stage('Unit Tests') {
            steps {
                echo '3. Executing Pytest unit tests...'
                sh '''
                    source ${VENV_NAME}/bin/activate
                    pytest --junitxml=reports/unit-test-results.xml tests
                '''
            }
        }
    }
    
    // Post-actions remain the same
    post {
        always {
            junit 'reports/unit-test-results.xml'
            cleanWs()
        }
        // ... (failure and unstable blocks removed for brevity, but they are useful!)
    }
}