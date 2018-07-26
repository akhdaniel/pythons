class JustCounter:
	__secretCounter = 0

	def count(self):
		self.__secretCounter += 1 
		print self.__secretCounter



counter = JustCounter()
counter.count()
counter.count()
counter.count()

print counter.__secretCounter

