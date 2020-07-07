from src.senseTask import SenseTask

import time
from res.container import Container as c


class AnimatedEmoji(SenseTask):
	SLEEP_TIME = 3
	def __init__(self):
		super().__init__()
	
	def execute(self):
		print (self.container.black)
		emojis = [c.emoji1, c.emoji2, c.emoji3]
		for e in emojis:
			self.sense.set_pixels(e)
			time.sleep(SLEEP_TIME)
		
