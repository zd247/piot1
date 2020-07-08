from datetime import datetime
from res.container import Container as c
from src.task_b.apiRESTful import ApiRESTful as api
from src.senseTask import SenseTask
import sqlite3
import time
import requests
import json


class MonitorAndNotify(SenseTask):
   ACCESS_TOKEN=""
   UPDATE_INTERVAL = 60
   
   def __init__ (self):
      super().__init__()
      self.conn = sqlite3.connect(c.dbname)
      self.sent = False
   

   # ===============================[task a]===============================
      
   def readDataFromSense(self):
      self.sense.clear()
      temp = self.sense.get_temperature()
      if temp is not None:
         temp = round(temp,1)

      self.sense.clear()
      humidity = self.sense.get_humidity()
      if  humidity is not None:
         humidity = round (humidity,1)
      
      return temp,humidity
   

   #==================================[task b]===================================
   #TODO: use cronjob to decide wether to send the notification instead using hard-coded variable

   def checkTempHumidity(self, temp, humidity):
      if temp < c.min or temp > c.max:
         body = "Comfortable temparature is out of range - sending from Raspberry Pi"
         self.pushNotification("Temparature alert", body)
      
      elif humidity < c.min or humidity > c.max:
         body = "Comfortable humidity is out of range - sending from Raspberry Pi"
         self.pushNotification("Humidity alert", body)
         
   
   
   def pushNotification(self, title, body):
      data_send = {"type": "note", "title": title, "body": body}

      res = requests.post('https://api.pushbullet.com/v2/pushes', 
                        data=json.dumps(data_send),
                        headers={'Authorization': 'Bearer ' + ACCESS_TOKEN, 
                        'Content-Type': 'application/json'})

      if res.status_code != 200:
         raise Exception('Something wrong')
      else:
         print('complete sending')
         self.sent = True

   
   #Override
   def execute(self):
      while True:
         api.postData(self.getData())
         time.sleep(UPDATE_INTERVAL)