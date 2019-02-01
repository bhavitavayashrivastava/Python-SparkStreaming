# code
Spark Streaming using Flume (pushed based Approach)
Flume - push data in HDFS (GOLDEN COPY) and SPARK STREAMING for further processing data and storing back into HDFS


##### SAMPLE_DATA  of WEBSERVER logs 
##### 192.168.100.4 - - [27/JAN/2019:04:09:08 +530] "GET /index.html HTTP/1.1" 304 - "-" "MOZILLA/5.0 (X11; Linux x86_64; rv:45.0) Geeko 20100101 Firefox/45.0"
##### 192.168.100.2 - - [27/JAN/2019:04:09:08 +530] "GET /index.html HTTP/1.1" 304 - "-" "MOZILLA/5.0 (WINDOWS NT 6.1; WIN64; x64) AppleWedKit/537.36 (KHTML LIKE Gecko) Chrome/71.800.56.0 Safari/537.36 
####
####
#########################################################################################################################################

###### to Run Flume AGENT 
 flume-ng agent -n sdc -f sdc.conf


##### TO RUN the Code have add jars at run-time from base directory 

##### spark-submit --jars "/usr/local/spark/jars/spark-streaming-flume-sink_2.11-2.3.2.jar,/usr/local/spark/jars/spark-streaming-flume_2.11-2.3.2.jar,/usr/locaL/spark/jars/spark-streaming-flume-assemble_2.11-2.3.2.jar,/usr/local/flume/lib/flume-ng-sdk-1.6.0.jar"
##### flumesparkStreaming.py 192.168.100.4 8123 /bhavi/
#####
#####
##### hostname = 192.168.100.4
##### port = 8123
##### outputPrefix = /bhavi/
