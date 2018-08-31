def functionName( level ):
	if level < 100:
		raise ValueError, level
	return level * 100



try:
	print 100/0
	print functionName(10)
except Exception as e:
	raise e
