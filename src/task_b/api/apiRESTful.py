from datetime import datetime
from res.container import Container as c
import sqlite3
import json

class ApiRESTful ():
   
   def getAllData(self):
      conn = sqlite3.connect(c.dbname)
      curs=conn.cursor()
      data = []
      for row in curs.execute("SELECT * FROM sense_table"):
         data.append(row)

      conn.close()
      
      return json.dumps(data)
         
      
   
   def getLastData(self):
      conn = sqlite3.connect(c.dbname)
      curs=conn.cursor()
      curs.execute("SELECT * FROM sense_table DESC LIMIT 1 ")
      data = curs.fetchone()

      ret = {}
      for key in curs.description:
         ret.update({key[0]: value for value in data})
         
      return json.dumps(data)
      

   def postData(self, temp, humidity):
      time = datetime.now()
      conn = sqlite3.connect(c.dbname)
      curs=conn.cursor()
      curs.execute("INSERT INTO sense_table values((?),(?),(?))", (time,temp,humidity,))
      conn.commit()
      conn.close()


   def updateLastData(self, temp, humidity):
      time = datetime.now()
      conn = sqlite3.connect(c.dbname)
      curs=conn.cursor()
      targetId = curs.rowcount()
      curs.execute ("UPDATE sense_table SET timestamp = (?) temp = (?) humidity = (?) WHERE id = (?)", 
      (time, temp, humidity, targetId))
      conn.commit()
      curs.close()
      conn.close()

   



      
   




