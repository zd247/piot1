import json
import sqlite3

class Container():
   CONFIG_DATA = json.load('config.json')

   def __init__(self):
      self.red = (255,0,0)
      self.green = (0,255,0)
      self.blue = (0,0,255)
      self.white = (150,150,150)
      self.yellow = (255,255,0)
      self.pink = (255,102,178)
      self.black = (0,0,0)
      self.brown = (51,0,0)
      self.purple = (102,0,102)

      # emojis
      self.emoji1  = [
      red,red,red,red,red,red,red,red,
      red,red,red,red,red,red,red,red,
      white,white,white,red,red,white,white,white,
      white,white,black,red,red,white,white,black,
      white,white,white,red,red,white,white,white,
      red,red,red,red,red,red,red,red,
      red,red,red,red,red,red,red,red,
      red,red,red,red,red,red,red,red
      ]

      self.emoji2  = [
      yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,
      yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,
      white,white,white,red,red,white,white,white,
      white,white,blue,red,red,white,white,blue,
      white,white,white,red,red,white,white,white,
      yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,
      yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,
      yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,
      ]

      self.emoji3 =[
      yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,
      yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,
      yellow,blue,blue,yellow,yellow,blue,blue,yellow,
      yellow,blue,blue,yellow,yellow,blue,blue,yellow,
      yellow,yellow,yellow,yellow,yellow,yellow, yellow,yellow,
      yellow,blue,blue,yellow,yellow,blue,blue,yellow,
      yellow,yellow,yellow,blue,blue,yellow,yellow,yellow,
      yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow
      ],

      self.dbname = "sense.db",
      self.table_name = "sense_table"

      
      self.min = CONFIG_DATA['comfortable_min']
      self.max = CONFIG_DATA['comfortable_max']


   def createTable(self):
      conn = sqlite3.connect(self.dbname)
      curs = conn.cursor() 
      curs.execute("DROP TABLE IF EXISTS (?)", (self.table_name))
      curs.execute("CREATE TABLE (?)(id INTEGER PRIMARY KEY AUTOINCREMENT,timestamp DATETIME, temp NUMERIC, humidity NUMERIC)",
      (self.table_name,))
      curs.close()
      conn.close()