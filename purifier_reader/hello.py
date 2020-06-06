import csv
import time
import yaml
import configReader
from datetime import datetime
from miio import AirPurifierMiot

configFile = "config.yaml"
ip = configReader.fetchIpAddress(configFile,"airpurifier")
token = configReader.fetchToken(configFile,"airpurifier")

air = AirPurifierMiot(ip,token)

while(True):
    prop = air.get_properties()
    dateTimeObj = datetime.now()

    
    #print(prop)

    temp = 0
    hum = 0
    aqi = 0

    for e in prop:
        if(e["did"] == "humidity"):
            hum = e["value"]
        if(e["did"] == "temperature"):
            temp = e["value"]
        if(e["did"] == "aqi"):
            aqi = e["value"]

    with open('data.csv', mode = 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #Timestamp, Temperatura, Umidità, AQI
        writer.writerow([round(time.time() * 1000),temp,hum,aqi])
        
    print(dateTimeObj)
    print(temp)
    print(hum)
    print(aqi)
    time.sleep(5.0)