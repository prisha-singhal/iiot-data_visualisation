
# IOT SENSOR DATA VISUALISATION

The goal is to visualize machine operations leveraging the Grafana+InfluxDB platform. InfluxDB is a
highly efficient open source time-series database that connects seamlessly with Grafana to aid in creating dashboards. This data is queried in Python to perform data analytics by filtering through it.


## Steps

   1. Install InfluxDB
   2. Install Grafana
   3. Write data into InfluxDB through python script 
   4. Add data source to Grafana through InfluxDB 

   


## Documentation

[InfluxDB installation](https://docs.influxdata.com/influxdb/v2/install/)

[Grafana installation](https://grafana.com/docs/grafana/latest/setup-grafana/installation/)

[Writing data using python](https://github.com/influxdata/influxdb-client-python#writes)

[Querying data](https://docs.influxdata.com/influxdb/cloud/api-guide/client-libraries/python/)

[Using Docker](https://www.youtube.com/watch?v=QGG_76OmRnA&t=188s)






## Familiar problems 

Creating timestamps and a readable dataframe for InfluxDB:
[Pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html)

[Another link](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html)


When connecting data source to Grafana:
[Github support](https://github.com/grafana/grafana/issues/32252#issuecomment-1776661324)
