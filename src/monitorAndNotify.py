from datetime import datetime
from res.container import Container as c
from src.senseTask import SenseTask
import sqlite3
import time
import requests
import json


class MonitorAndNotify(SenseTask):
   ACCESS_TOKEN=""
   
   def __init__ (self):
      super().__init__()
      self.conn = sqlite3.connect(c.dbname)
      self.sent = False
   

   # ===============================[task a]===============================
   def createTable(self):
      curs = self.conn.cursor() 
      curs.execute("DROP TABLE IF EXISTS (?)", (c.table_name))
      curs.execute("CREATE TABLE (?)(id INTEGER PRIMARY KEY AUTOINCREMENT,timestamp DATETIME, temp NUMERIC, humidity NUMERIC)",
      (c.table_name,))

      
   def getData(self):
      time = datetime.now().strftime("%H:%M")

      self.sense.clear()
      temp = self.sense.get_temperature()
      if temp is not None:
         temp = round(temp,1)

      self.sense.clear()
      humidity = self.sense.get_humidity()
      if  humidity is not None:
         humidity = round (humidity,1)
      
      return time,temp,humidity
   

   def saveData(self):
      time,temp,humidity = self.getData()
      curs=self.conn.cursor()
      curs.execute("INSERT INTO (?) values((?),(?),(?))", (c.table_name,time,temp,humidity,))
      self.conn.commit()
      if (self.sent is False):
         self.checkTempHumidity(temp,humidity)

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
      self.createTable()
      while True:
         saveData()
         time.sleep(60)
      self.conn.close()