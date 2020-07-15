from res.container import Container as c
from res.helper import Helper as h
from src.task_b.api.apiRESTful import ApiRESTful as api
from sense_hat import SenseHat
import sqlite3
import time
import requests
import json


# Auto
class MonitorAndNotify():   
   def __init__ (self):
      self.sense = SenseHat()
      self.sent = False
      self.api = api()
   

   # ===========[1]=============
      
   def readDataFromSense(self):
      self.sense.clear()
      t1 = self.sense.get_temperature_from_humidity()
      t2 = self.sense.get_temperature_from_pressure()
      t_cpu = h.get_cpu_temp()

      # Calculates the real temperature compesating CPU heating.
      t = (t1 + t2) / 2
      temp = t - ((t_cpu - t)/ 1.5)
      # temp = h.get_smooth(temp)
      if temp is not None:
         temp = round(temp,1)



      self.sense.clear()
      humidity = self.sense.get_humidity()
      if  humidity is not None:
         humidity = round (humidity,1)
      
      return temp,humidity
   

   #==============[2]==========
   

   def checkTempHumidityAndPush(self, temp, humidity):
      if temp < c.min or temp > c.max:
         body = "Comfortable temparature is out of range - sending from Raspberry Pi"
         self.pushNotification("Temparature alert", body)
      
      elif humidity < c.min or humidity > c.max:
         body = "Comfortable humidity is out of range - sending from Raspberry Pi"
         self.pushNotification("Humidity alert", body)
         
   
   #TODO: use cronjob to decide wether to send the notification instead using hard-coded variable
   def pushNotification(self, title, body):
      if (self.sent is False):
         data_send = {"type": "note", "title": title, "body": body}

         res = requests.post('https://api.pushbullet.com/v2/pushes', 
                           data=json.dumps(data_send),
                           headers={'Authorization': 'Bearer ' + c.access_token, 
                           'Content-Type': 'application/json'})

         if res.status_code != 200:
            raise Exception('Something wrong')
         else:
            print('complete sending')
            self.sent = True

   
   #Override
   def execute(self):
      while True:
         temp, humidity = self.readDataFromSense()
         self.api.postData(temp, humidity)
         self.checkTempHumidityAndPush(temp, humidity)
         time.sleep(c.update_interval)