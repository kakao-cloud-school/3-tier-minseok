pipeline {
    agent any
    triggers {
        githubPush() // GitHub에 커밋이 발생하면 자동으로 파이프라인 시작
    }
    environment {
        REPOSITORY = "innnnnwoo"
        DOCKERHUB_CREDENTIALS = credentials('docker_accesstkn')
        IMAGE_TAG = "${env.BUILD_NUMBER}"
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
                      def image = docker.build('innnnnwoo/web:${IMAGE_TAG}', '.')
                    }
                    dir('imagemaker/'){
                      def image = docker.build('innnnnwoo/imagemaker:${IMAGE_TAG}', '.')
                    }
                    dir('was/'){
                      def image = docker.build('innnnnwoo/jenkinshub:${IMAGE_TAG}', '.')
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
                    sh "docker push innnnnwoo/web:${IMAGE_TAG}"
                    sh "docker push innnnnwoo/imagemaker:${IMAGE_TAG}"
                    sh "docker push innnnnwoo/jenkinshub:${IMAGE_TAG}"
                }
            }
        }
        stage('Update yaml'){
            steps {
                script{
                    sh "sed -i 's|image: innnnnwoo/web/.*|image: innnnnwoo/web:${IMAGE_TAG}|' yaml/7_nginx-deploy.yaml"
                    sh "sed -i 's|image: innnnnwoo/imagemaker/.*|image: innnnnwoo/imagemaker:${IMAGE_TAG}|' yaml/10_imagemaker_deploy.yaml"
                    sh "sed -i 's|image: innnnnwoo/jenkinshub/.*|image: innnnnwoo/jenkinshub:${IMAGE_TAG}|' yaml/6_django_deploy.yaml"
                }
            }
        }
        stage('Commit Updated yaml') {
            steps {
                script {
                    sh """
                        git config user.name "dada0013"
                        git config user.email "yoon351200@naver.com"
                        git add yaml/*.yaml
                        git commit -m "Update image tags to ${IMAGE_TAG}"
                        git push origin main
                    """
                }
            }
        }
    }
}
