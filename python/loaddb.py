#!/usr/bin/env python

#Developer : Sunish Surendran Kannembath
#Reach me out in LinkedIn : https://www.linkedin.com/in/sunishsurendrank/
#Reach me out in Twitter : @sunishsurendran

#Objective of the Script is to Read Data From the CSV file and Write into the InlfuxDB

import pandas as pd
import datetime
import os
from influxdb import InfluxDBClient

print("------Running loaddb Python Script-------")

#Initializing the variables
Scriptpath = os.getcwd()
Projectpath = os.path.dirname(Scriptpath)
date = datetime.date.today()
formatted_date = datetime.date.strftime(date, "%m-%d-%Y")
file_path = r"{0}\COVID-19\csse_covid_19_data\csse_covid_19_daily_reports\{1}.csv".format(Projectpath,formatted_date)


#Checking the Path exist, if not check with previous day from current date
if(os.path.exists(file_path)):
    print("File exist")
else:
    yesterday = datetime.date.today() - datetime.timedelta(1)
    formatted_date = datetime.date.strftime(yesterday, "%m-%d-%Y")
    file_path = r"{0}\COVID-19\csse_covid_19_data\csse_covid_19_daily_reports\{1}.csv".format(Projectpath,formatted_date)

#Printing the File Path
print (file_path)

#Reading from CSV File
csvReader = pd.read_csv(file_path)

#Client Object Created to connect the InfluxDB
client = InfluxDBClient(host='localhost',port=8086)
client.create_database('COVID19Report')
client.switch_database('COVID19Report')

#For loop to Convert the Data read from CSV to JSON body.
#JSON will be written to the Database

for row_index, row in csvReader.iterrows() :
    country=row[3]
    confirmed = row[7]
    deaths = row[8]
    recovered =row[9]
    latitude =row[5]
    longitude =row[6]


    json_body = [
        {
            "measurement": "COVID19Report",
            "tags": {
                "country":country,
                "confirmed": confirmed,
                "deaths": deaths,
                "recovered": recovered,
            },
            "fields": {
                "countryname": country,
                "confirmed": confirmed,
                "deaths": deaths,
                "recovered": recovered,
                "latitude":latitude,
                "longitude":longitude
            }
        }

    ]
    try:
        client.write_points(json_body)
        #print(json_body)

    except:
        print("error:Error happened while writing  to the Database")

print(row_index)





