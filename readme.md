# hotline

[![​Gitpod Ready-to-Code​](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://GitHub.com/sannae/hotline) 
​[![​Open in Visual Studio Code​](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/sannae/hotline)

### Continuous integration

![Build Docker image](https://github.com/sannae/hotline/actions/workflows/build-docker-image.yml/badge.svg)

### Manually use me

Manually build me: `docker build -t hotline .`

Manually run me: `docker run --name hotline -p 8000:8000 -d hotline`

Pull from public DockerHub: `docker pull sannae/hotline:latest`

Troubleshoot if port forward is not working: `docker logs hotline`
