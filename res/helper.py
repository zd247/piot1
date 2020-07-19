# Reference: https://raspberrypi.stackexchange.com/questions/61524/how-to-approximate-room-temperature-in-a-better-way

import os
from res.container import Container as c
import time
import calendar
import requests
import json

class Helper():

   # Get CPU temperature.
   def get_cpu_temp(self):
      res = os.popen("vcgencmd measure_temp").readline()
      return float(res.replace("temp=","").replace("'C\n",""))


   def verify_send_time(self):
      res = requests.get('https://api.pushbullet.com/v2/pushes',
                       headers={'Authorization': 'Bearer ' + c.access_token} )
      pushes = json.loads(res.text).get('pushes')
      lastestPush = list(pushes)[0]
      # print(json.dumps(lastPush, indent = 4)) # formatter to view
      lastestPushTime = lastestPush.get('created')
      # print (lastestPushTime, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(lastestPushTime))) # see lastest push time
      currentTime = calendar.timegm(time.gmtime())

      if (currentTime >= lastestPushTime + c.day_in_sec):
         return True
      
      return False

   # # Use moving average to smooth readings.
   # def get_smooth(x):
   #    if not hasattr(get_smooth, "t"):
   #       get_smooth.t = [x,x,x]
   #    get_smooth.t[2] = get_smooth.t[1]
   #    get_smooth.t[1] = get_smooth.t[0]
   #    get_smooth.t[0] = x
   #    xs = (get_smooth.t[0]+get_smooth.t[1]+get_smooth.t[2])/3
   #    return(xs)
