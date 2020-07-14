from src.task_a.animatedEmoji import AnimatedEmoji
from src.task_b.monitorAndNotify import MonitorAndNotify
from src.task_b.readAndDisplay import ReadAndDisplay
from src.task_b.createReport import CreateReport
from src.task_b.api.apiTest import ApiTest
from res.container import Container as c
import sqlite3

class Main:
   @staticmethod
   def main():
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

      #### task a
      # AnimatedEmoji().execute()

      #### task b
      # MonitorAndNotify().execute()
      # ReadAndDisplay().execute()
      # CreateReport().execute()
      # ApiTest().execute()


Main.main()