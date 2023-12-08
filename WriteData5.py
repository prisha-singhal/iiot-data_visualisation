import pandas as pd
#import matplotlib.pyplot as plt 
import numpy as np 
from datetime import datetime, timedelta

table1 = pd.read_excel(r'/Users/prishasinghal/Desktop/TMF_Part_Fingerprint_dataset/part_train.xlsx',sheet_name=['sheet1','sheet2','sheet3','sheet4'])
# print(type(table1))
# print(table1["sheet3"])

#export INFLUXDB_TOKEN=sLja1tiOPVxKf4BCRgNOmSOFGXdpfK5UEfCC8FAS5USWWnshDBIXuDdmRPD1FkviSf2CQX525JewOE6xGbyL-A==
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = "sLja1tiOPVxKf4BCRgNOmSOFGXdpfK5UEfCC8FAS5USWWnshDBIXuDdmRPD1FkviSf2CQX525JewOE6xGbyL-A=="
org = "VIP research"
url = "http://localhost:8086"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
bucket="NewBucket"

write_api = client.write_api(write_options=SYNCHRONOUS)
# for value in range(5):
#   point = (
#     Point("measurement1")
#     .tag("tagname1", "tagvalue1")
#     .field("field1", value)
#   )
#   write_api.write(bucket=bucket, org="VIP research", record=point)
#   time.sleep(1) # separate points by 1 second

_now = datetime(2023,11,29,0,0,0)-timedelta(days=2)
print(_now)
ts = [_now]
for time in range(1,len(table1["sheet4"])+1):
    ts.append(_now + (time*timedelta(seconds=10)))
ts_dataFrame = pd.DataFrame(ts,columns =["timeStamp"])
# print(ts_dataFrame)


# data_frame = pd.DataFrame(data=[["coyote_creek", 1.0], ["coyote_creek", 2.0]],
#                                    index=[_now, _now + timedelta(hours=1)],
#                                    columns=["location", "water_level"])
data_frame = table1["sheet4"]
data_frame.rename( columns={'Unnamed: 0':'timeStamp',"418-3272_30":"currentValue"}, inplace=True )
data_frame['timeStamp'] = ts_dataFrame['timeStamp']
# data_frame['timeStamp'] = data_frame['timeStamp'].replace(data_frame['timeStamp'], ts_dataFrame)
data_frame.set_index('timeStamp',inplace=True)

print(data_frame)


write_api.write(bucket, org, record=data_frame, data_frame_measurement_name="418-3272_30")
  