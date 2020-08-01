from sense_hat import SenseHat
from res.container import Container as c
import random
import time


class ElectronicDie():
   def __init__ (self):
      self.sense = SenseHat()


   def shake():
      acceleration = self.sense.get_accelerometer_raw()
      x = acceleration['x']
      y = acceleration['y']
      z = acceleration['z']

      vx = abs(x)
      vy = abs(y)
      vz = abs(z)
      time.sleep(0.1)
      x,y,z = self.sense.get_accelerometer_raw().values()

      x1 = abs(abs(vx)-abs(x))
      y1 = abs(abs(vy)-abs(y))
      z1 = abs(abs(vz)-abs(z))

      if x1 > 0.5 or y1 > 0.5 or z1 > 0.5:
         global n
         n = random.randint(1,6)
         if n == 1:
            sense.set_pixels(c.one)
            return n
         if n == 2:
            sense.set_pixels(c.two)
            return n
         if n == 3:
            sense.set_pixels(c.three)
            return n
         if n == 4:
            sense.set_pixels(c.four)
            return n
         if n == 5:
            sense.set_pixels(c.five)
            return n
         if n == 6:
            sense.set_pixels(c.six)
            return n
      
      return 0