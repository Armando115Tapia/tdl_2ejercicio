import dweepy
import requests
import json
from twisted.internet import task, reactor

## Define time
timeout = 60.0  # Sixty seconds

## 15 Minutes
# timeout = 60.0 * 15  # Sixty seconds

## URL to make post 
urlComplete='http://localhost:5000/tempHum'
#urlComplete='https://backendtodolegal.herokuapp.com/tempHum'

urlWebHook='https://webhook.site/bb5a6abe-1a7b-452e-86c8-40b2bbba00b7'

## Lambda function
dict_lamb = lambda: dweepy.get_dweets_for('thecore')[0]


## Execute every 15 minutes
def doWork():
    #do work here
    tempC = dict_lamb()['content']['temperature']
    hum = dict_lamb()['content']['humidity']
    infoTempHum = {"temperature":tempC,"humidity":hum}
    response = requests.post(urlComplete, json = infoTempHum)
    #hit the webhook 
    responseWebHook = requests.post(urlWebHook, json = infoTempHum)
    print(response.json()) 
    pass

l = task.LoopingCall(doWork)
l.start(timeout) 

reactor.run()


