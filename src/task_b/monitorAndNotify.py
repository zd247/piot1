from res.container import Container as c
from res.helper import Helper as h
from src.task_b.api.apiRESTful import ApiRESTful as api
from sense_hat import SenseHat
import sqlite3
import time
import calendar
import requests
import json


# Auto
class MonitorAndNotify():   
   def __init__ (self):
      self.sense = SenseHat()
      self.sent = False
      self.api = api()
      self.h = h()
   

   # ===========[1]=============
      
   def readDataFromSense(self):
      self.sense.clear()
      t1 = self.sense.get_temperature_from_humidity()
      t2 = self.sense.get_temperature_from_pressure()
      t_cpu = self.h.get_cpu_temp()

      # Calculates the real temperature compesating CPU heating.
      t = (t1 + t2) / 2
      temp = t - ((t_cpu - t)/ 1.5)
      # temp = h.get_smooth(temp) // weird syntax, doesnt work
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
         self.pushNotification("Temparature alert", c.bad_temp_msg)
      elif humidity < c.min or humidity > c.max:
         self.pushNotification("Humidity alert", c.bad_humidity_msg)
         
   
   # use cronjob to decide wether to send the notification instead using hard-coded variable
   def pushNotification(self, title, body):
      if (self.h.verify_send_time() is True):
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