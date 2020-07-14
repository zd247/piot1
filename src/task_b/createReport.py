import json
from src.task_b.monitorAndNotify import MonitorAndNotify as mntf
from res.container import Container as c


class CreateReport():
   def __init__(self):
      self.mntf = mntf()


   def readDailyData(self):
      temp, humidity = self.mntf.readDataFromSense()
   
