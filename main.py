from src.task_a.animatedEmoji import AnimatedEmoji
from src.task_b.readAndDisplay import ReadAndDisplay
from src.task_b.createReport import CreateReport
from src.task_d.electronicDie import ElectronicDie
from src.task_d.game import Game
from res.container import Container as c

class Main:
   @staticmethod
   def main():
      task = input("Please enter a task to run (a,b,d): ")
      if (task is 'a'):
         AnimatedEmoji().execute()
      elif (task is 'b'):
         task_b = input ('Please enter a number to run sub task b (3,4): ')
         if (task_b == '3'):
            ReadAndDisplay().execute()
         elif (task_b == '4'):
            CreateReport().execute()
         else:
            print ("Wrong input format, please run the program again and input correctly")
      elif (task is 'd'):
         task_d = input ('Please enter a number to run sub task b (1,2): ')
         if (task_d is '1'):
            ElectronicDie().execute()
         elif (task_d is '2'):
            Game().execute()
         else:
            print ("Wrong input format, please run the program again and input correctly")
      else:
         print ("Wrong input format, please run the program again and input correctly")

Main.main()