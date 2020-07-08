# Reference: http://yaab-arduino.blogspot.com/2016/08/display-two-digits-numbers-on-raspberry.html

from src.senseTask import SenseTask
from src.task_b.apiRESTful import ApiRESTful as api
from res.container import Container as c
import sqlite3
import time
import json


class ReadAndDisplay(SenseTask):
   UPDATE_INTERVAL = 60
   OFFSET_LEFT = 1
   OFFSET_TOP = 2
   NUMS =[1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,  # 0
         0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,  # 1
         1,1,1,0,0,1,0,1,0,1,0,0,1,1,1,  # 2
         1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,  # 3
         1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,  # 4
         1,1,1,1,0,0,1,1,1,0,0,1,1,1,1,  # 5
         1,1,1,1,0,0,1,1,1,1,0,1,1,1,1,  # 6
         1,1,1,0,0,1,0,1,0,1,0,0,1,0,0,  # 7
         1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,  # 8
         1,1,1,1,0,1,1,1,1,0,0,1,0,0,1]  # 9

   def __init__(self):
      super().__init__()
      self.dataCount = self.countCurrentRowNum()
      

   def countCurrentRowNum(self):
      conn = sqlite3.connect(c.dbname)
      curs=conn.cursor()
      count = curs.rowcount()
      conn.close()
      
      return count

   # Displays a single digit (0-9)
   def showDigit(self,val, xd, yd, r, g, b):
      offset = val * 15
      for p in range(offset, offset + 15):
         xt = p % 3
         yt = (p-offset) // 3
         self.sense.set_pixel(xt+xd, yt+yd, r*NUMS[p], g*NUMS[p], b*NUMS[p])

   # Displays a two-digits positive number (0-99)
   def showNumber(self,val, r, g, b):
      abs_val = abs(val)
      tens = abs_val // 10
      units = abs_val % 10
      if (abs_val > 9): self.showDigit(tens, OFFSET_LEFT, OFFSET_TOP, r, g, b)
      self.showDigit(units, OFFSET_LEFT+4, OFFSET_TOP, r, g, b)
   
      
   def displayTemparature(self):
      data = json.loads(api.getLastData())[0]
      temp = data['temp']

      # set color
      r,g,b = c.green
      if (temp > c.max): r,g,b = c.red
      elif (temp < c.min): r,g,b = c.blue
      #display
      self.showNumber(temp, r,g,b)
   

   def execute(self):
      self.sense.clear()
      self.displayTemparature()
      while True:
         currentCount = self.countCurrentRowNum()
         # update the display if there's a new record
         if currentCount > self.dataCount:
            self.displayTemparature()
            self.dataCount = currentCount # update global row count

         time.sleep(UPDATE_INTERVAL)

      self.sense.clear()
      
   
