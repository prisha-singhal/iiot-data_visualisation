
import pandas as pd #importing libraries as requird 
import numpy as np 
from datetime import datetime, timedelta
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS #importing influxdb client library to write data from python into influxdb  

table1 = pd.read_excel(r'/Users/prishasinghal/Desktop/TMF_Part_Fingerprint_dataset/part_train.xlsx',sheet_name=['sheet1','sheet2','sheet3','sheet4'])
token = "sLja1tiOPVxKf4BCRgNOmSOFGXdpfK5UEfCC8FAS5USWWnshDBIXuDdmRPD1FkviSf2CQX525JewOE6xGbyL-A=="
org = "VIP research"
url = "http://localhost:8086" #defining API token, and organisation for InfluxDB (flux language)
client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
bucket="NewBucket" #bucket into which the data will be written into 
# _now = datetime(2023,10,29,0,0,0)-timedelta(days=2) #creating timestamps for data. It is required for InfluxDB as it deals with time series data
# ts = [_now]

def write_data(sheet,sensorID):
    _now = datetime(2023,10,29,0,0,0)-timedelta(days=2) #creating timestamps for data. It is required for InfluxDB as it deals with time series data
    ts = [_now]
    write_api = client.write_api(write_options=SYNCHRONOUS) #writing data into the bucket 

    for time in range(1,len(table1[sheet])+1): # adding timestamps that are 10s apart for two days for each data point 
        ts.append(_now + (time*timedelta(seconds=10)))
        ts_dataFrame = pd.DataFrame(ts,columns =["timeStamp"])
        data_frame = table1[sheet]
        data_frame.rename( columns={'Unnamed: 0':'timeStamp',sensorID:"currentValue"}, inplace=True ) #adding column names for dataset (flux language)
        data_frame['timeStamp'] = ts_dataFrame['timeStamp']
        data_frame.set_index('timeStamp',inplace=True)

    write_api.write(bucket, org, record=data_frame, data_frame_measurement_name = sensorID)
    print(data_frame)
    

write_data(sheet = "sheet4",sensorID = "418-3272_30")
# write_data(sheet = "sheet3",sensorID = "3T-6742_32")
# write_data(sheet = "sheet2",sensorID = "346-9011_30")
# write_data(sheet = "sheet1",sensorID = "5T-5977_30")

# query = '''SHOW COLUMNS FROM 418-3272_30'''
#     table = client.query(query=query, language ='sql', mode='pandas')
#     print(table)
# query = '''SHOW COLUMNS FROM 418-3272_30'''
# table = client.query(query=query, language ='sql', mode='pandas')
# print(table)

# table1 = pd.read_excel(r'/Users/prishasinghal/Desktop/TMF_Part_Fingerprint_dataset/part_train.xlsx',sheet_name=['sheet1','sheet2','sheet3','sheet4'])
# print(type(table1))
#print(table1["sheet4"]) #reading data from excel into python and converting it into a table 
