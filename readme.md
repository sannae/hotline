# hotline

### Continuous integration

![Build Docker image](https://github.com/sannae/hotline/actions/workflows/build-docker-image.yml/badge.svg)

### Manually use me

Manually build me: `docker build -t hotline .`

Manually run me: `docker run --name hotline -p 8000:8000 -d hotline`

Pull from public DockerHub: `docker pull sannae/hotline:latest`

Troubleshoot if port forward is not working: `docker logs hotline`
