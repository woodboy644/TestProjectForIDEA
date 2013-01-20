import random

class Greeting:
	def __init__(self):
		pass

	def howAreYou(self):
		select = random.randint(1, 100)
		if select <= 50:
			print "I'm fine. Thank you!"
		else:
			print "I'm not fine, now..."

