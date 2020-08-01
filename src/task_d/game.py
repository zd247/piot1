from sense_hat import SenseHat
from src.task_d.electronicDie import ElectronicDie
import random
import time
import csv
from datetime import datetime 

class Game():
   def __init__(self):
      self.sense = SenseHat()
      self.eDie = ElectronicDie()


   def execute(self):
      self.sense.clear()
      #self.sense.show_message("Pressed middle button to start. Who reached 30 points with the dice first is the winner", scroll_speed = 0.03)
      #self.sense.show_message("When finished rolling, pressed the middle button to save the score and pass to the next player", scroll_speed = 0.03)
     
      p1points = 0
      p2points = 0
      ppointer = True
      global temp
      temp = 1

      while True:
         if ppointer:
            n = self.eDie.shake()
            if n != 0:
             temp = n
            if n == 0: 
             n = temp 
            for event in self.sense.stick.get_events():
               if (event.direction, event.action) == ('middle', 'released'):
                  p1points = p1points + n
                  ppointer = False
                  self.sense.show_message("P1: " + format(p1points) + " P2: " + format(p2points), scroll_speed = 0.03)
                  if p1points >= 30:
                     now = datetime.now()
                     current_time = now.strftime("%H:%M:%S")
                     self.sense.show_message("P1 won at " + format(current_time) + "! Pressed middle button to save your score", scroll_speed = 0.03)
                     with open('record.csv', 'w', newline ='') as file:
                        writer = csv.writer(file)
                        writer.writerow(["P1 won", p1points, current_time])
         
         else:
            n = self.eDie.shake()
            if n != 0:
             temp = n
            if n == 0: 
             n = temp 
            for event in self.sense.stick.get_events():
               if (event.direction, event.action) == ('middle', 'released'):
                  p2points = p2points + n
                  ppointer = True
                  self.sense.show_message("P1: " + format(p1points) + " P2: " + format(p2points), scroll_speed = 0.03)
                  if p2points >= 30:
                     now = datetime.now()
                     current_time = now.strftime("%H:%M:%S")
                     self.sense.show_message("P2 won at " + format(current_time) + "! Pressed middle button to save your score", scroll_speed = 0.03)
                     with open('/home/pi/iot/winnerRec/winner.csv', 'a', newline ='') as file:
                        writer = csv.writer(file)
                        writer.writerow(["P2 won", p2points, current_time])


 