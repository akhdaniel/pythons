


try:
	fo = open("data.txt", "r")
	content = fo.read()
	data = content.split("\n")
	print data

	a = 0
	b = 100

	c = b / a 

	print c

except IOError, e:
	print "File tidak ditemukan"
	print e 

except ZeroDivisionError as e:
	print "pembagian dengan 0!!"
	print e

except Exception as e:
	raise e

finally:
	print "selesai proses dan except"

