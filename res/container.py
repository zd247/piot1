import json
import sqlite3

class Container():
   CONFIG_DATA = json.load(open('./res/config.json'))
   config_min_max_data = json.load(open('./res/config_min_max.json'))

   r = (255,0,0)
   g = (0,255,0)
   b = (0,0,255)
   w = (150,150,150)
   y = (255,255,0)

   # emojis
   emoji1  = [
   w,w,w,w,w,w,w,w,
   w,w,r,w,w,g,w,w,
   w,w,r,w,w,g,w,w,
   w,w,r,w,w,g,w,w,
   w,w,w,w,w,w,w,w,
   w,w,b,w,w,b,w,w,
   w,w,w,b,b,w,w,w,
   w,w,w,w,w,w,w,w,
   ]

   emoji2  = [
   w,w,w,w,w,w,w,w,
   w,y,y,w,w,g,g,w,
   w,y,y,w,w,g,g,w,
   w,w,w,w,w,w,w,w,
   w,w,w,b,b,w,w,w,
   w,w,w,w,w,w,w,w,
   w,w,w,r,r,w,w,w,
   w,w,r,r,r,r,w,w,
   ]

   emoji3 =[
   b,b,b,g,g,b,b,b,
   b,b,r,r,y,y,b,b,
   b,r,r,r,y,y,y,b,
   b,r,r,r,y,y,y,b,
   b,r,r,r,y,y,y,b,
   b,b,r,r,y,y,b,b,
   b,b,r,r,y,y,b,b,
   b,b,b,r,y,b,b,b,
   ]

   dbname = "sense.db"
   table_name = "sense_table"

   sleep_time = 3
   update_interval = 60
   

   access_token = "o.NH9RJ56RPc2U7SNTORUWTksCk4SBRCY0"

   
   min = CONFIG_DATA['comfortable_min']
   max = CONFIG_DATA['comfortable_max']

   day_in_sec = 86400

   csv_file_name = 'report.csv'

   degree_sign = u"\N{DEGREE SIGN}"

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


      

