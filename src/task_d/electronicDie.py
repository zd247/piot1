from sense_hat import SenseHat
from res.container import Container as c
import random
import time


class ElectronicDie():
   def __init__ (self):
      self.sense = SenseHat()


   def shake(self):
      global n
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
         n = random.randint(1,6)
         if n == 1:
            self.sense.set_pixels(c.one)
         if n == 2:
            self.sense.set_pixels(c.two)
         if n == 3:
            self.sense.set_pixels(c.three)
         if n == 4:
            self.sense.set_pixels(c.four)
         if n == 5:
            self.sense.set_pixels(c.five)
         if n == 6:
            self.sense.set_pixels(c.six)
      else:
        n = 0
      return n

   def execute(self):
      while True:
         self.shake()
        