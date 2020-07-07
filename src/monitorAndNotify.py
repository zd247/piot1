from sense_hat import SenseHat
import sqlite3
import datetime
import time
from res.container import Container

class MonitorAndNotify():
   def __init__ (self):
      self.sense = SenseHat()
      self.c = Container()
      self.conn = sqlite3.connect(c.dbname)
   
   def createTable(self):
      curs = self.conn.cursor() 
      curs.execute("DROP TABLE IF EXISTS sense_table")
      curs.execute("CREATE TABLE sense_table(timestamp DATETIME, temp NUMERIC, humidity NUMERIC)")

      
   def getData(self):
      time = datetime.datetime.now()
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
      curs.execute("INSERT INTO sense_table values(time,temp,humidity)", (temp,))
      self.conn.commit()
   
   def execute(self):
      while True:
         saveData()
         time.sleep(60)
      self.conn.close()