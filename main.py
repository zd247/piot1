from src.task_a.animatedEmoji import AnimatedEmoji
from src.task_b.monitorAndNotify import MonitorAndNotify
from res.container import Container as c
import sqlite3

class Main:
   @staticmethod
   def main():
      conn = sqlite3.connect(c.dbname)
      curs = conn.cursor() 
      curs.execute("DROP TABLE IF EXISTS sense_table")
      curs.execute(
         "CREATE TABLE sense_table ("
         
         "timestamp DATETIME,"
         "temp NUMERIC," 
         "humidity NUMERIC)")
      curs.close()
      conn.close()

      # task a
      # AnimatedEmoji().execute()

      # task b
      # (1)
      MonitorAndNotify().execute()
   
      



Main.main()