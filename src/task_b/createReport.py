from src.task_b.monitorAndNotify import MonitorAndNotify as mntf
from src.task_b.api.apiRESTful import ApiRESTful as api
from res.container import Container as c
from datetime import datetime
import json
import csv

class CreateReport():
   def __init__(self):
      self.mntf = mntf()
      self.api = api()


   def readAndSaveData(self):
      temp, humidity = self.mntf.readDataFromSense()
      self.api.postData(temp, humidity) # save to database
      date = datetime.now().strftime("%d/%m/%Y")
      with open ('report.csv', 'w', newline = '') as file:
         writer = csv.writer(file)
         writer.writerow([date, temp])


      
   def execute(self):
      self.readAndSaveData()

