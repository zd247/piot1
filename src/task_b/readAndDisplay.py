# Reference: http://yaab-arduino.blogspot.com/2016/08/display-two-digits-numbers-on-raspberry.html

from sense_hat import SenseHat
from src.task_b.api.apiRESTful import ApiRESTful as api
from res.container import Container as c
import sqlite3
import time
import json


class ReadAndDisplay():
   def __init__(self):
      self.sense = SenseHat()
      self.dataCount = self.countCurrentRowNum()
      self.api = api()
      

   def countCurrentRowNum(self):
      conn = sqlite3.connect(c.dbname)
      curs=conn.cursor()
      count = len(curs.fetchall())
      conn.close()
      
      return count

   # Displays a single digit (0-9)
   def showDigit(self,val, xd, yd, r, g, b):
      offset = val * 15
      for p in range(offset, offset + 15):
         xt = p % 3
         yt = (p-offset) // 3
         self.sense.set_pixel(xt+xd, yt+yd, r*c.nums[p], g*c.nums[p], b*c.nums[p])

   # Displays a two-digits positive number (0-99)
   def showNumber(self,val, r, g, b):
      abs_val = abs(val)
      tens = abs_val // 10
      units = abs_val % 10
      if (abs_val > 9): self.showDigit(tens, c.offset_left, c.offset_top, r, g, b)
      self.showDigit(units, c.offset_left+4, c.offset_top, r, g, b)
   
      
   def displayTemparature(self):
      data = json.loads(self.api.getLastData())
      temp = int(round(data[2]))
      
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
         if currentCount > self.dataCount: # update the display if there's a new record detected
            self.displayTemparature()
            self.dataCount = currentCount # update global row count

         time.sleep(c.update_interval)

      self.sense.clear()
      
   
