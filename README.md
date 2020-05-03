# COVID19Dashboard

# Prerequisites
-User should have basic knowledge of python

-Install Python in you machine

-Install following Python Dependencies 
  -pip3 install influxdb
  -pip3 install pandas
  
-Install git in your machine
  
 -Docker should be installed in your machine 
   -User can follow below link to install 
   https://docs.docker.com/docker-for-windows/install/
   
 #Step 1
 
 1.git clone https://github.com/sunishsurendrank/COVID19Dashboard.git
 
 Navigate to the cloned folder
 
2. git clone https://github.com/CSSEGISandData/COVID-19.git

#Step 2

Open PowerShell in the windows machine run Docker command


#Step 3

Run the python Script
docker run -d --name=influxdb -p 8086:8086  influxdb

cd "\Python Script"
python loaddb.py

#Step 4

docker run -d --name=grafana -p 3000:3000 sunishsurendrank/grafanaimage:v1

#Step 5

Open Chrome and access http://localhost:300

