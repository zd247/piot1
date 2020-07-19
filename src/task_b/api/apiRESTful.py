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
      data = curs.execute("SELECT * FROM sense_table ORDER BY id DESC LIMIT 1").fetchone()
      return json.dumps(data)
      

   def postData(self, temp, humidity):
      time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
      conn = sqlite3.connect(c.dbname)
      curs=conn.cursor()
      curs.execute("INSERT INTO sense_table(timestamp, temp, humidity) VALUES ((?),(?),(?))", (time,temp,humidity,))
      conn.commit()
      conn.close()


   def updateLastData(self, temp, humidity):
      time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
      conn = sqlite3.connect(c.dbname)
      curs=conn.cursor()
      data = json.loads(self.getLastData())
      targetId = data[0]
      curs.execute("UPDATE sense_table SET timestamp = (?), temp = (?), humidity = (?) WHERE id = (?)", (time,temp,humidity,targetId))
      conn.commit()
      curs.close()
      conn.close()

   



      
   




