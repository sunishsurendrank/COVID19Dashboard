# How to deploy the COVID19DashBoard Project in your machine

This documentation willl help user to Install the application in user windows machine.This documentation steps are more focused on windows platform.

- Author of this Document : Sunish Surendran Kannembath
- Developer : Sunish Surendran Kannembath
- Reach Sunish in LinkedIn : https://www.linkedin.com/in/sunishsurendrank/
- Reach Sunish in Twitter : @sunishsurendran

## Prerequisites before trying the project
- User should have basic knowledge of Python.

- Install Python in your machine.

- Install following Python Dependencies 
  - pip3 install influxdb
  - pip3 install pandas
  
- Install git in your machine
  
- Docker should be installed in your machine 
   -User can follow below link to install Docker in your machine
   https://docs.docker.com/docker-for-windows/install/

## Get started with the COVID19Dashboard Project
   
  ## Step 1
  
  - git clone https://github.com/sunishsurendrank/COVID19Dashboard.git
  
  - Navigate to the cloned folder
  
  - git clone https://github.com/CSSEGISandData/COVID-19.git

  ## Step 2

  - Open PowerShell in the windows machine run Docker command
  -Run below commnd to download the InfluxDB Docker Image from DockerHub and run it
    - docker run -d --name=influxdb -p 8086:8086  influxdb

  ## Step 3

  - Run the python Script
    - cd "\Python Script"
    - python loaddb.py

  ## Step 4
  - Run below commnd to download the Grafana Docker Image from DockerHub and run it
    - docker run -d --name=grafana -p 3000:3000 sunishsurendrank/grafanaimage:v1

  ## Step 5

  - Open Chrome and access http://localhost:3000

![dashboard](https://user-images.githubusercontent.com/12937248/80937013-fa589c00-8df0-11ea-8367-b98cc3d9d289.PNG)


