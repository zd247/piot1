from src.task_b.monitorAndNotify import MonitorAndNotify
from src.task_b.api.apiTest import ApiTest
from src.task_c.bluetooth import Bluetooth
from res.container import Container as c
import sqlite3

class Auto:
   @staticmethod
   def run():
      conn = sqlite3.connect(c.dbname)
      curs = conn.cursor() 
      # curs.execute("DROP TABLE IF EXISTS sense_table")
      curs.execute(
         "CREATE TABLE IF NOT EXISTS sense_table ("
         "id INTEGER PRIMARY KEY AUTOINCREMENT,"
         "timestamp DATETIME,"
         "temp NUMERIC," 
         "humidity NUMERIC)")
      curs.close()
      conn.close()

      ApiTest().execute()
      # MonitorAndNotify().execute()
      # Bluetooth().execute()
     


Auto.run()