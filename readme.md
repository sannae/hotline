# hotline

[![​Gitpod Ready-to-Code​](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://GitHub.com/sannae/hotline) 
​[![​Open in Visual Studio Code​](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/sannae/hotline)

## Main features

* Perform CRUD operations on customers, products, tickets, technical personnel
* Perform CRUD operations on projects and project steps and assign them to a specific customer
* Link project steps or tickets to a calendar

## Continuous integration

![Build Docker image](https://github.com/sannae/hotline/actions/workflows/build-docker-image.yml/badge.svg)

The CI/CD pipeline is handled using a [GitHub Actions workflow](./.github/workflows/build-docker-images.yml).

The workflow is divided into three sequential jobs (`test`, `build` and `deploy`).

The `test` job will:

* Create the list of dependencies using `pip freeze`
* Install the listed dependencies 
* Perform all the tests with the [Django testing suite](https://docs.djangoproject.com/en/4.0/topics/testing/)
* Measure code coverage using [coverage.py](https://coverage.readthedocs.io/en/6.3/)

The `build` job will:

* Run the `update-version.sh` script to update the patch version
* Run the `clean-images.sh` script to remove older local images from Docker
* Build the latest Docker image
* Tag the images with the version number

The `deploy` job will:

* Prepare the code for deployment by using the proper settings
* Run the Django built-in deployment checklist
* Push the `:latest` and the versioned image to DockerHub registry
* Clean up the local Docker environment by deleting the older images


