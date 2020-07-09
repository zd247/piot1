import time
from res.container import Container as c
from sense_hat import SenseHat

class AnimatedEmoji():
	
	def __init__(self):
		self.sense = SenseHat()
	
	def execute(self):
		emojis = [c.emoji1, c.emoji2, c.emoji3]
		while True:
			self.sense.clear()
			for e in emojis:
				self.sense.set_pixels(e)
				time.sleep(c.sleep_time)
		
