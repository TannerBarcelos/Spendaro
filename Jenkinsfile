pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building docker images for production'
            }
        }
        stage('Test and Lint') {
            steps {
                echo 'Running Tests (Unit, Integration, E2E)'
            }
        }
        stage('Publish to Docker Hub') {
            steps {
                echo 'Publishing docker images to docker hub'
            }
        }
        stage('Package as Artifact') {
            steps {
                echo 'Packaging spendaro as artifact for fail-safe deployment and backup'
            }
        }
        stage('Deploy to Staging') {
            steps {
                echo 'Deploying to staging on AWS EKS staging cluster'
            }
        }
        // deploy to production only if tests pass and staging deployment is successful
        stage('Deploy to Production') {
            steps {
                echo 'Deploying to production on AWS EKS prod cluster'
            }
        }

    }
}
// UNDER CONSTRUCTION