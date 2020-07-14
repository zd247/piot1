from src.task_b.api.apiRESTful import ApiRESTful as api
from sense_hat import SenseHat
from res.container import Container as c

# auto
class ReadAndDisplay():
   def __init__(self):
      self.sense = SenseHat()
      self.api = api()
      
   
   def execute(self):
      return 0