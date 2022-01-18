# hotline

[![​Gitpod Ready-to-Code​](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://GitHub.com/sannae/hotline) 
​[![​Open in Visual Studio Code​](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/sannae/hotline)

## Main features

* Perform CRUD operations on customers, products, tickets, technical personnel
* Perform CRUD operations on projects and project steps and assign them to a specific customer
* Link project steps or tickets to a calendar

## Continuous integration

![Build Docker image](https://github.com/sannae/hotline/actions/workflows/build-docker-image.yml/badge.svg)

### Build

Build Docker image:
```bash
docker build -t hotline .
```

### Deployment

Pull image from Docker Hub and run container: 
```bash
docker run --name hotline -p 8000:8000 -d sannae/hotline:latest`
```

