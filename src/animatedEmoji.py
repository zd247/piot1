from sense_hat import SenseHat
import time
from res.container import Container


class AnimatedEmoji():
	SLEEP_TIME = 3
	def __init__(self):
		self.c = Container()
		self.sense = SenseHat()
	
	def execute(self):
		print (self.container.black)
		emojis = [c.emoji1, c.emoji2, c.emoji3]
		for e in emojis:
			self.sense.set_pixels(e)
			time.sleep(SLEEP_TIME)
		
