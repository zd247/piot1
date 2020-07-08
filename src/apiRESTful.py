from datetime import datetime
from res.container import Container as c
import sqlite3
import json

class ApiRESTful ():
   
   def getAllData(self):
      conn = sqlite3.connect(c.dbname)
      curs=conn.cursor()
      data = []
      for row in curs.execute("SELECT * FROM (?)", (c.table_name,)):
         data.append(row)
      
      return json.dumps(data)
         
      
   
   def getLastData(self):
      conn = sqlite3.connect(c.dbname)
      curs=conn.cursor()
      curs.execute("SELECT * FROM (?) ORDER BY id DESC LIMIT 1 ", (c.table_name))
      data = curs.fetchone()

      # ret = {}
      # for key in curs.description:
      #    ret.update({key[0]: value for value in data})
         
      return json.dumps(data)
      

   def postData(self, temp, humidity):
      time = datetime.now().strftime("%H:%M")
      conn = sqlite3.connect(c.dbname)
      curs=conn.cursor()
      curs.execute("INSERT INTO (?) values((?),(?),(?))", (c.table_name,time,temp,humidity,))
      conn.commit()
      conn.close()


   def updateLastData(self, temp, humidity):
      time = datetime.now().strftime("%H:%M")
      conn = sqlite3.connect(c.dbname)
      curs=conn.cursor()
      targetId = curs.rowcount()
      curs.execute ("UPDATE (?) SET timestamp = (?) temp = (?) humidity = (?) WHERE id = (?)", 
      (c.table_name, time, temp, humidity, targetId))
      conn.commit()
      curs.close()
      conn.close()

   



      
   




