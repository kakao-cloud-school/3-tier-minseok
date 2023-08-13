pipeline {
    agent any
    triggers {
        githubPush() // GitHub에 커밋이 발생하면 자동으로 파이프라인 시작
    }
    environment {
        REPOSITORY = "joyoungkyung/jenkinshub"
        DOCKERHUB_CREDENTIALS = credentials('docker_access_token')
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/kakao-cloud-school/3-tier-minseok.git'
            }
        }
        stage('Build') {
            steps {
                script {
                    dir('web/'){
                      def image = docker.build('joyoungkyung/jenkinshub:web2', '.')
                    }
                    dir('was/'){
                      def image = docker.build('joyoungkyung/jenkinshub', '.')
                    }
                    dir('imagemaker/'){
                      def image = docker.build('joyoungkyung/jenkinshub:imagemaker', '.')
                    }
                }
            }
        }
        stage('Docker Login') {
            steps {
                script {
                    def credentials = credentials('docker_access_token')
                    sh "echo \$DOCKERHUB_CREDENTIALS_PSW | docker login -u \$DOCKERHUB_CREDENTIALS_USR --password-stdin"
                }
            }
        }
        stage('Docker Push') {
            steps {
                script {
                    sh "docker push joyoungkyung/jenkinshub:web2"
                    sh "docker push joyoungkyung/jenkinshub"
                    sh "docker push joyoungkyung/jenkinshub:imagemaker"
                }
            }
        }
    }
}
