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

   def createCSVfile(self, fileName):
      open(fileName, "a")
      with open (fileName, "r+") as file:
         reader = csv.reader(file)
         writer = csv.writer(file)

         lineCount = 0
         for row in reader:
            lineCount += 1
            if lineCount > 0: 
               return
         
         writer.writerow(['Date', 'Status'])


   def readLastDataFromCSV (self, fileName):
      data = {}
      with open (fileName, "r") as file:
         reader = csv.reader(file, delimiter=',')
         lineCount = 0
         for row in reader:
            if lineCount == 0: lineCount += 1
            else:
               data['date'] = row[0]
               data['status'] = row[1]
               lineCount += 1
      
      return data

   def saveData(self, date, temp, humidity):
      self.api.postData(temp, humidity) # save to database
      
      #write to csv
      status = ''
      if temp < c.min:
         offset = round(c.min - temp)
         status = "BAD: {} {} C below the comfort temperature".format(offset, c.degree_sign)
      elif temp > c.max:
         offset = round(temp - c.max)
         status = "BAD: {} {} C above the comfort temperature".format(offset, c.degree_sign)
      else:
         status = "OK"

      with open (c.csv_file_name, 'a' , newline = '') as file:
         writer = csv.writer(file)
         writer.writerow([date, status])


   def readAndSaveData(self):
      temp, humidity = self.mntf.readDataFromSense()

      currentDate = datetime.now().strftime("%m/%d/%Y")
      lastSavedDate = self.readLastDataFromCSV(c.csv_file_name).get('date')
      if (lastSavedDate is None): self.saveData(currentDate, temp, humidity)
      else: 
         if (currentDate > lastSavedDate): self.saveData(currentDate, temp,humidity)
         


      
   def execute(self):
      self.createCSVfile(c.csv_file_name)
      self.readAndSaveData()
      

