pipeline {
    agent any
    triggers {
        githubPush() // GitHub에 커밋이 발생하면 자동으로 파이프라인 시작
    }
    environment {
        REPOSITORY = "innnnnwoo"
        DOCKERHUB_CREDENTIALS = credentials('docker_accesstkn')
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
                      def image = docker.build('innnnnwoo/web', '.')
                    }
                    dir('imagemaker/'){
                      def image = docker.build('innnnnwoo/imagemaker', '.')
                    }
                    dir('was/'){
                      def image = docker.build('innnnnwoo/jenkinshub', '.')
                    }
                }
            }
        }
        stage('Docker Login') {
            steps {
                script {
                    def credentials = credentials('docker_accesstkn')
                    sh "echo \$DOCKERHUB_CREDENTIALS_PSW | docker login -u \$DOCKERHUB_CREDENTIALS_USR --password-stdin"
                }
            }
        }
        stage('Docker Push') {
            steps {
                script {
                    sh "docker push innnnnwoo/web"
                    sh "docker push innnnnwoo/imagemaker"
                    sh "docker push innnnnwoo/jenkinshub"
                }
            }
        }
    }
}
