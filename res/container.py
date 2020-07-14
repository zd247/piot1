import json
import sqlite3

class Container():
   CONFIG_DATA = json.load(open('./res/config.json'))

   red = (255,0,0)
   green = (0,255,0)
   blue = (0,0,255)
   white = (150,150,150)
   yellow = (255,255,0)
   pink = (255,102,178)
   black = (0,0,0)
   brown = (51,0,0)
   purple = (102,0,102)

   # emojis
   emoji1  = [
   red,red,red,red,red,red,red,red,
   red,red,red,red,red,red,red,red,
   white,white,white,red,red,white,white,white,
   white,white,black,red,red,white,white,black,
   white,white,white,red,red,white,white,white,
   red,red,red,red,red,red,red,red,
   red,red,red,red,red,red,red,red,
   red,red,red,red,red,red,red,red
   ]

   emoji2  = [
   yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,
   yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,
   white,white,white,red,red,white,white,white,
   white,white,blue,red,red,white,white,blue,
   white,white,white,red,red,white,white,white,
   yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,
   yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,
   yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,
   ]

   emoji3 =[
   yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,
   yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,
   yellow,blue,blue,yellow,yellow,blue,blue,yellow,
   yellow,blue,blue,yellow,yellow,blue,blue,yellow,
   yellow,yellow,yellow,yellow,yellow,yellow, yellow,yellow,
   yellow,blue,blue,yellow,yellow,blue,blue,yellow,
   yellow,yellow,yellow,blue,blue,yellow,yellow,yellow,
   yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow
   ]

   dbname = "sense.db"
   table_name = "sense_table"

   sleep_time = 3
   update_interval = 60
   

   access_token = "o.NH9RJ56RPc2U7SNTORUWTksCk4SBRCY0"

   
   min = CONFIG_DATA['comfortable_min']
   max = CONFIG_DATA['comfortable_max']
   

   offset_left = 1
   offset_top = 2
   nums =[1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,  # 0
         0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,  # 1
         1,1,1,0,0,1,0,1,0,1,0,0,1,1,1,  # 2
         1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,  # 3
         1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,  # 4
         1,1,1,1,0,0,1,1,1,0,0,1,1,1,1,  # 5
         1,1,1,1,0,0,1,1,1,1,0,1,1,1,1,  # 6
         1,1,1,0,0,1,0,1,0,1,0,0,1,0,0,  # 7
         1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,  # 8
         1,1,1,1,0,1,1,1,1,0,0,1,0,0,1]  # 9

