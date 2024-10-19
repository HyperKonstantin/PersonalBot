
properties([disableConcurrentBuilds()])

pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage("Info") {
            steps {
                whoami
                pwd
                ls -la
            }
        }
        stage("build image") {
            steps {
                docker rm -f bot
                docker build -t bot .
            }
        }
        stage("deploy") {
            steps {
                docker run -d bot
            }
        }
    }
}