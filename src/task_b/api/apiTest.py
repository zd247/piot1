from src.task_b.api.apiRESTful import ApiRESTful as api
from sense_hat import SenseHat
from res.container import Container as c
import json

# auto
class ReadAndDisplay():
   def __init__(self):
      self.sense = SenseHat()
      self.api = api()
      self.testPasses = [False, False, False, False]

   def testGetAllData(self): 
      data = self.api.getAllData()
      if (data.count > 0 or data is not None):
         print (data)
         self.testPasses[0] = True

   def testGetLastData (self):
      data = self.api.getLastData()
      if (data is not None):
         print (data)
         self.testPasses[1] = True
   
   def testPostData(self):
      self.api.postData(9999,9999)
      newData = json.loads(self.api.getLastData())[0]
      if (newData['temp'] is 9999 and newData['humidity'] is 9999):
         self.testPasses[2] = True
      
   def testUpdateLastData(self):
      self.api.updateLastData(6666, 8888)
      lastData = json.loads(self.api.getLastData())[0]
      if (lastData['temp'] is 6666 and lastData['humidity'] is 8888):
         self.testPasses[3] = True
   

   def execute(self):
      self.testGetAllData()
      self.testGetLastData()
      self.testPostData()
      self.testUpdateLastData()

      count = 0
      for i in range (self.testPasses.count):
         if (self.testPasses[i] is True):
            count += 1
      
      print ("Number of test passes {}/{}".format(count, self.testPasses.count))
      return