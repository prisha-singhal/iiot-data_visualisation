import influxdb_client, os, time
import numpy as np
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import pandas as pd

client = influxdb_client.InfluxDBClient(url="http://localhost:8086", token="sLja1tiOPVxKf4BCRgNOmSOFGXdpfK5UEfCC8FAS5USWWnshDBIXuDdmRPD1FkviSf2CQX525JewOE6xGbyL-A==", org="adea8e270e3f09e0")

query_api = client.query_api()
query = ('''
                          from(bucket: "NewBucket")
   |> range(start: -30d, stop: now())
   |> filter(fn: (r) => r["_measurement"] == "346-9011_30")
   |> filter(fn: (r) => r["_field"] == "currentValue")
   |> filter(fn: (r) => r._value > 4.0)
   |> aggregateWindow(every: 10s, fn: mean, createEmpty: false)
   |> yield(name: "mean")
                         |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
                         ''')
result = query_api.query_data_frame(org="adea8e270e3f09e0", query=query)
results = []
# pd.set_option('display.max_columns', None)
# print(result)

for table in result:
  print(table)
  # for record in table.records:
  #   print(record.values)
  #   results.append(( record.get_value(), record.get_time()))
print(table.columns.values)
selected_columns = table[['_time', 'currentValue']]

new_df = pd.DataFrame(selected_columns)
new_df.set_index('_time',inplace=True)
print(new_df)

#writing data
bucket="ReadData_Bucket"

write_api = client.write_api(write_options=SYNCHRONOUS)
# new_results = pd.DataFrame.from_dict(results)
# new_results.set_index('timeStamp',inplace=True)

write_api.write(bucket, org="adea8e270e3f09e0", record=new_df, data_frame_measurement_name='CurrentValues>4.0')





# df=pd.DataFrame(result)
# print(df)
# print(results)
# data = {results}
# print(new_results)
# custom_index = ['Field','Value','Time']
# new_results = new_results.set_index(pd.Index(custom_index))
# print(new_results)

# data = [results]
# df=pd.Dataframe(data, columns=['currentValue',''])
# for table in results:
#   print(table)
#   for record in table.records:
#     # print(record.values)
#     results.append((record.get_value()))

#  print(results)

# tables = query_api.query('''
#                          from(bucket: "NewBucket")
#   |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
#   |> filter(fn: (r) => r["_measurement"] == "346-9011_30")
#   |> filter(fn: (r) => r["_field"] == "currentValue")
#   |> aggregateWindow(every: 10s, fn: mean, createEmpty: false)
#   |> yield(name: "mean")
#                          ''')
# for table in tables:
#  print(table)
 
#  query = """from(bucket: "NewBucket")
#  |> range(start: -10m)
#  |> filter(fn: (r) => r._measurement == "3T-6742_32")"""

# "adea8e270e3f09e0"