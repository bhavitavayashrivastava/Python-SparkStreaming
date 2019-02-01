# code
Spark Streaming using Flume (pushed based Approach)


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
