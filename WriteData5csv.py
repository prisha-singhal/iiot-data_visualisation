import pandas as pd
import numpy as np 
from datetime import datetime, timedelta

table = pd.read_csv("3T-6742_30.csv")
print(table)

import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = "ANR31z25bpsj-JxDpAe3I3VhVBdwEaFP5qVYIz7DLVH0LTlDO3DrdJ_3ugctWrHhLQHCPKVrKOW60VFuWNZqhw=="
org = "adea8e270e3f09e0"
url = "http://localhost:8086"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
bucket="NewBucket"

write_api = client.write_api(write_options=SYNCHRONOUS)


_now = datetime(2023,11,29,0,0,0)-timedelta(days=2)
ts = [_now]
for time in range(1,len(table)+1):
    ts.append(_now + (time*timedelta(seconds=10)))
ts_dataFrame = pd.DataFrame(ts,columns =["timeStamp"])
# print(ts_dataFrame)


# data_frame = table
data_frame = table
# data_frame.columns = ['timeStamp','currentValue']
data_frame['timeStamp'] = ts_dataFrame['timeStamp']
# data_frame.rename( columns={'Unnamed: 0':'timeStamp',"3T-6742_30":"currentValue"}, inplace=True )

# # data_frame['timeStamp'] = data_frame['timeStamp'].replace(data_frame['timeStamp'], ts_dataFrame)
data_frame.rename( columns={'2.866':'currentValue'},inplace=True)
data_frame.set_index('timeStamp',inplace=True)

print(data_frame)


write_api.write(bucket, org, record=data_frame, data_frame_measurement_name='3T-6742_30')