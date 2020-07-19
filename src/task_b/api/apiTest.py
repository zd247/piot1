from src.task_b.api.apiRESTful import ApiRESTful as api
from sense_hat import SenseHat
from res.container import Container as c
import sqlite3
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
      conn = sqlite3.connect(c.dbname)
      curs=conn.cursor()
      count = curs.execute("SELECT count(*) FROM sense_table").fetchone()[0]
      conn.close()

      data = json.loads(self.api.getAllData())
      if (len(data) == count):
         logging.debug ("getAllData passed !")
         self.testPasses[0] = True
         return True
      return False

   def testGetLastData (self):
      conn = sqlite3.connect(c.dbname)
      curs=conn.cursor()
      count = curs.execute("SELECT count(*) FROM sense_table").fetchone()[0]
      conn.close()

      data = json.loads(self.api.getLastData())
      if (data[0] == count):
         logging.debug ("getLastData passed !")
         self.testPasses[1] = True
         return True

      return False
   
   def testPostData(self):
      self.api.postData(9999,9999)
      
      if (self.testGetLastData() == False): return False

      newData = json.loads(self.api.getLastData())
      if (newData[2] == 9999 and newData[3] == 9999):
         logging.debug ("postData passed !")
         self.testPasses[2] = True
         return True
      return False
      
   def testUpdateLastData(self):
      self.api.updateLastData(6666, 8888)
      lastData = json.loads(self.api.getLastData())
      if (lastData[2] == 6666 and lastData[3] == 8888):
         logging.debug ("updateLastData passed !")
         self.testPasses[3] = True
         return True
         
      return False
   

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