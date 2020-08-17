import dweepy
import requests
import json
from twisted.internet import task, reactor

## Define time
timeout = 60.0  # Sixty seconds

## URL to make post 
urlComplete='http://localhost:5000/tempHum'

## Lambda function
dict_lamb = lambda: dweepy.get_dweets_for('thecore')[0]


## Execute every 15 minutes
def doWork():
    #do work here
    tempC = dict_lamb()['content']['temperature']
    hum = dict_lamb()['content']['humidity']
    infoTempHum = {"temperature":tempC,"humidity":hum}
    response = requests.post(urlComplete, json = infoTempHum)
    print(response.json()) 
    pass

l = task.LoopingCall(doWork)
l.start(timeout) # call every sixty seconds

reactor.run()


