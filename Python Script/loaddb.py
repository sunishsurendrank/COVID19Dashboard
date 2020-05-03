#!/usr/bin/env python

import pandas as pd
import datetime
import os
from influxdb import InfluxDBClient


print("------Running Python Script-------")

today = datetime.date.today()
formatted_date = datetime.date.strftime(today, "%m-%d-%Y")
file_path = r"E:\Github\COVID19 Dashboard\COVID-19\csse_covid_19_data\csse_covid_19_daily_reports\{}.csv".format(formatted_date)
print(file_path)
if(os.path.exists(file_path)):
    print("File exist")
else:
    yesterday = datetime.date.today() - datetime.timedelta(1)
    formatted_date = datetime.date.strftime(yesterday, "%m-%d-%Y")
    file_path = r"E:\Github\COVID19 Dashboard\COVID-19\csse_covid_19_data\csse_covid_19_daily_reports\{}.csv".format(formatted_date)


print (file_path)
csvReader = pd.read_csv(file_path)

client = InfluxDBClient(host='localhost',port=8086)
client.create_database('COVID19Report')
client.switch_database('COVID19Report')

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
        print(json_body)

    except:
        print("------Error-------")

#Write to InfluxDB





