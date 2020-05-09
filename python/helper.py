
import datetime
import requests
import pandas as pd
import os

def Download_latest_CSV():
    # Downloading the latest CSV file from the Git Repo
    date = datetime.date.today()
    formatted_date = datetime.date.strftime(date, "%m-%d-%Y")
    while True:

        filename = r"{0}.csv".format(formatted_date)
        downloadurl = r"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{0}".format(
            filename)
        print(downloadurl)
        file = requests.get(downloadurl)
        if (file.status_code != 404):
            print("Found the file with date", formatted_date)
            break

        print("Unable to find the file with date", formatted_date)
        yesterday = date - datetime.timedelta(1)
        date = yesterday
        formatted_date = datetime.date.strftime(yesterday, "%m-%d-%Y")

    open(filename, 'wb').write(file.content)
    return filename

def Read_CSV(filename):
    # Checking the Path exist, if not check with previous day from current date
    if (os.path.exists(filename)):
        csvReader = pd.read_csv(filename)
        return csvReader
    else:
        raise Exception("Failed to find the file in",filename)

def Create_Data_JSON(csvReader):
    json_body = []
    errorcount = 0
    for row_index, row in csvReader.iterrows():
        country = row[3]
        confirmed = row[7]
        deaths = row[8]
        recovered = row[9]
        latitude = row[5]
        longitude = row[6]
        # Handling NaN
        if str(row[5]) == 'nan':
            latitude = 0.0
        if str(row[6]) == 'nan':
            longitude = 0.0
        try:
            json_body += [
                {
                    "measurement": "COVID19Report",
                    "tags": {
                        "index": row_index,
                        "country": country,
                        "confirmed": confirmed,
                        "deaths": deaths,
                        "recovered": recovered,
                    },
                    "fields": {
                        "confirmed": confirmed,
                        "countryname": country,
                        "deaths": deaths,
                        "recovered": recovered,
                        "latitude": latitude,
                        "longitude": longitude
                    }
                }
            ]

        except:
            errorcount += 1
            print("error:Error happened while creating the json Object - {}".format(row_index))
    print("Found {} data objects".format(row_index+1))
    return json_body



