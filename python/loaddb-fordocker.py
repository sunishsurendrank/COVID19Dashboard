#!/usr/bin/env python

#Developer : Sunish Surendran Kannembath
#Reach me out in LinkedIn : https://www.linkedin.com/in/sunishsurendrank/
#Reach me out in Twitter : @sunishsurendran

#Objective of the Script is to Read Data From the CSV file and Write into the InlfuxDB

from influxdb import InfluxDBClient
import time
import helper
print("------Running loaddb Python Script-------")

while True:
    filename = helper.Download_latest_CSV()
    csvReader = helper.Read_CSV(filename)
    json_body = helper.Create_Data_JSON(csvReader)
    totalcount = len(json_body)

    # JSON will be written to the Database
    print("Updating {} records in database..".format(totalcount))

    # Client Object Created to connect the InfluxDB
    client = InfluxDBClient(host='influxdb', port=8086)
    client.create_database('COVID19Report')
    client.switch_database('COVID19Report')
    client.write_points(json_body)
    client.close()
    print("Updated {} records in the database".format(totalcount))
    print("Script will run tommorrow..")
    time.sleep(24.0 * 60.0 * 60.0)


