pipeline {
    agent any
    
    environment {
        VENV = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/<your-github-username>/<repo-name>.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh 'python3 -m venv $VENV'
                sh 'source $VENV/bin/activate'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '$VENV/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '$VENV/bin/pytest test_case.py'
            }
        }

        stage('Deploy to Staging') {
            when {
                branch 'main'
            }
            steps {
                sh 'echo "Deploying application..."'
                sh 'nohup python3 app.py &'
            }
        }
    }

    post {
        success {
            mail to: 'your-email@example.com',
                 subject: "Build Successful",
                 body: "The Jenkins pipeline executed successfully."
        }
        failure {
            mail to: 'your-email@example.com',
                 subject: "Build Failed",
                 body: "The Jenkins pipeline failed. Please check the logs."
        }
    }
}
