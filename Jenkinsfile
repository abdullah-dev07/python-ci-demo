// Jenkinsfile (Declarative Pipeline for Python CI)

pipeline {
    // 1. Agent: Use a specific Docker image to ensure a clean, consistent Python environment.
    agent {
        docker {
            image 'python:3.11-slim' // Uses the Python 3.11 image
        }
    }
    
    // Environment variables for path safety
    environment {
        VENV_NAME = 'venv' // Name of the virtual environment directory
    }

    stages {
        
        stage('Setup Environment') {
            steps {
                echo '1. Setting up Python virtual environment and dependencies...'
                
                // Create a virtual environment
                sh 'python -m venv ${VENV_NAME}'
                
                // Activate venv and install dependencies from requirements.txt
                // The '.' command is shorthand for 'source' in shell scripts
                sh '. ${VENV_NAME}/bin/activate && pip install --upgrade pip'
                sh '. ${VENV_NAME}/bin/activate && pip install -r requirements.txt'
            }
        }
        
        stage('Code Quality (Lint)') {
            steps {
                echo '2. Running Flake8 Linter for code style checks...'
                // flake8 checks for PEP 8 compliance and complexity
                // --exclude excludes the auto-generated venv directory
                // || true allows the pipeline to proceed even if linting fails
                sh '. ${VENV_NAME}/bin/activate && flake8 --exclude=${VENV_NAME} . || true'
            }
        }

        stage('Unit Tests') {
            steps {
                echo '3. Executing Pytest unit tests...'
                // pytest runs the tests, generating an XML report for Jenkins
                // The 'tests' argument tells pytest where to look for tests
                sh '. ${VENV_NAME}/bin/activate && pytest --junitxml=reports/unit-test-results.xml tests'
            }
        }
    }
    
    // Post-actions run after all stages, typically for cleanup and reporting.
    post {
        always {
            // Archive the JUnit XML report so Jenkins can display the test results graphically
            junit 'reports/unit-test-results.xml'
            
            // Clean up the workspace files after the build is done
            cleanWs()
        }
        failure {
            echo 'Pipeline FAILED! One or more stages or tests did not pass.'
        }
        unstable {
            echo 'Pipeline UNSTABLE! Tests ran but there were test failures (check JUnit report).'
        }
        success {
            echo 'Pipeline SUCCESS! All tests and checks passed. Code is ready for deployment!'
        }
    }
}