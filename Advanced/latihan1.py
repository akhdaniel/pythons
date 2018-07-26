class latihan:

	# def __init__(self):
	# 	pass

	def reverse_words(self, s):
		# words = s.split(" ")
		# rev = reversed(words)
		return " ".join(reversed(s.split(" ")))


lat = latihan()
print lat.reverse_words("hello world python")
