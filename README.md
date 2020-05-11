[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![contributions welcome](https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square)](https://github.com/TheAlgorithms/Python/blob/master/CONTRIBUTING.md)&nbsp;

# How to deploy the COVID19DashBoard Project in your machine

This documentation willl help user to Install the application in user windows machine.This documentation steps are more focused on windows platform.

- Author of this Document : Sunish Surendran Kannembath
- Developer : Sunish Surendran Kannembath
- Reach Sunish in LinkedIn : https://www.linkedin.com/in/sunishsurendrank/
- Reach Sunish in Twitter : @sunishsurendran

## Architecture Diagram
![architecture_diagram_10-5-2020](https://user-images.githubusercontent.com/12937248/81503251-3499d000-9300-11ea-9f87-e46db5e74358.png)

## Comparison with old architecture Diagram
![architecture_comparision](https://user-images.githubusercontent.com/12937248/81503256-382d5700-9300-11ea-84dc-53fced953e27.PNG)

## Prerequisites before trying the project

- Docker should be installed in your machine 
   -User can follow below link to install Docker in your machine
   https://docs.docker.com/docker-for-windows/install/

## Get started with the COVID19Dashboard Project
   
  ## Step 1
   - Open PowerShell in the windows machine run Docker command
   - Create a Private network for Docker with name COVID19DashboardbNetwork
        - docker network create COVID19DashboardbNetwork
   
  ## Step 2
  - Run below command to download the InfluxDB Docker Image from DockerHub and run as a container
    - docker run -d -p 8086:8086 --network COVID19DashboardbNetwork --name influxdb influxdb

  ## Step 3

  - Run below commnd to download the Python Script image from DockerHub and run as a container
    - docker run -d -p 3000:3000 --network COVID19DashboardbNetwork --name=pythonimage sunishsurendrank/pythonimage:v1

  ## Step 4
  - Run below commnd to download the Grafana Docker Image from DockerHub and run as a container
    - docker run -d -p 3000:3000 --network COVID19DashboardbNetwork --name=grafana sunishsurendrank/grafanaimage:v1

  ## Step 5

  - Open Chrome and access http://localhost:3000

![dashboard](https://user-images.githubusercontent.com/12937248/80937013-fa589c00-8df0-11ea-8367-b98cc3d9d289.PNG)

 ## License
 Copyright © 2020, [Sunish Surendran Kannembath](https://github.com/sunishsurendrank). 
 Released under the [MIT License](LICENSE).
 





