// Jenkinsfile — the recipe book for Jenkins (the robot helper).
// Jenkins reads this file top to bottom, stage by stage.
// A stage only starts after the one before it finishes.

pipeline {
    agent any

    environment {
        // The label (tag) on the lunchbox. Same label everywhere.
        IMAGE_TAG = 'shop-app:1.0.0'
    }

    stages {
        stage('Checkout') {
            steps {
                // Bring the latest code from GitHub.
                checkout scm
            }
        }
        stage('Build') {
            steps {
                // Get ready: install the test tool.
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                // Run the  tests. This stage is a GATE:
                // if a test fails, Jenkins stops here and
                // the Docker image is never built.
                sh 'PYTHONPATH=. python -m pytest -q'
            }
        }
        stage('Build Docker image') {
            steps {
                // Pack the app into a Docker image (the lunchbox).
                // This stage only runs because Test passed above.
                sh 'docker build -t shop-app:1.0.0 .'
            }
        }
        stage('Package') {
            steps {
                // Keep a copy of the packed app files as proof.
                // (Real cloud deploy is a later step, not in this project.)
                sh 'tar -czf shop-app-1.0.0.tar.gz app'
                archiveArtifacts artifacts: 'shop-app-1.0.0.tar.gz'
            }
        }
    }

    post {
        success {
            echo 'All stages passed. Docker image shop-app:1.0.0 is ready.'
        }
        failure {
            echo 'A stage failed. Check which stage, fix it, and run again.'
        }
    }
}
