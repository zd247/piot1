from src.task_b.api.apiRESTful import ApiRESTful as api
from sense_hat import SenseHat
from res.container import Container as c
import json
import time
import logging

# auto
class ApiTest():
   def __init__(self):
      self.sense = SenseHat()
      self.api = api()
      self.testPasses = [False, False, False, False]
      logging.basicConfig(filename="API_test.log", level=logging.DEBUG)

   def testGetAllData(self): 
      data = json.loads(self.api.getAllData())
      if (len(data) > 0 or data is not None):
         logging.debug ("getAllData passed !")
         self.testPasses[0] = True

   def testGetLastData (self):
      data = json.loads(self.api.getLastData())
      if (data is not None):
         logging.debug ("getLastData passed !")
         self.testPasses[1] = True
   
   def testPostData(self):
      self.api.postData(9999,9999)
      newData = json.loads(self.api.getLastData())
      if (newData[2] == 9999 and newData[3] == 9999):
         logging.debug ("postData passed !")
         self.testPasses[2] = True
      
   def testUpdateLastData(self):
      self.api.updateLastData(6666, 8888)
      lastData = json.loads(self.api.getLastData())
      if (lastData[2] == 6666 and lastData[3] == 8888):
         logging.debug ("updateLastData passed !")
         self.testPasses[3] = True
   

   def execute(self):
      with open('API_test.log', 'w'):
         pass
      self.testGetAllData()
      time.sleep(0.2)
      self.testGetLastData()
      time.sleep(0.2)
      self.testPostData()
      time.sleep(0.2)
      self.testUpdateLastData()
      time.sleep(0.2)

      count = 0
      for i in range (len(self.testPasses)):
         if (self.testPasses[i] is True):
            count += 1
      
      logging.debug ("Number of test passes {}/{}".format(count, len(self.testPasses)))