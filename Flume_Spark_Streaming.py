##### SAMPLE_DATA
##### 192.168.100.4 - - [27/JAN/2019:04:09:08 +530] "GET /index.html HTTP/1.1" 304 - "-" "MOZILLA/5.0 (X11; Linux x86_64; rv:45.0) Geeko 20100101 Firefox/45.0"
##### 192.168.100.2 - - [27/JAN/2019:04:09:08 +530] "GET /index.html HTTP/1.1" 304 - "-" "MOZILLA/5.0 (WINDOWS NT 6.1; WIN64; x64) AppleWedKit/537.36 (KHTML LIKE Gecko) Chrome/71.800.56.0 Safari/537.36 
####
####
#####

from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.flume import FlumeUtils

import sys 
hostname = sys.argv[1]
port =   int(sys.argv[2])

conf = SparkConf().setAppName("Flume Spark Streaming").setMaster("local[2]")

sc = SparkContext(conf = conf)

ssc = StreamingContext(sc,30)

agents = [(hostname, port)]

pollingStream = FlumeUtils.createPollingStream(ssc,agents)

messages = pollingStream.map(lambda msg: msg[1])

osmessage = messages.filter(lambda msg: msg.split(" ")[13])

osnames = osmessage.map(lambda msg: (msg.split(" ")[12],1))

from operator import add 

osCount = osnames.reduceByKey(add)

outputPrefix = sys.argv[3]

osCount.pprint()           # to print on console

osCount.saveAsTextFiles(outputPrefix)

ssc.start()
ssc.awaitTermination()
