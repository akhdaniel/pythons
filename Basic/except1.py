try:
	fh = open("/opt/file.txt","w")
	fh.write("This is my test file for exception handling!!")
except Exception, e:
	print "Error: ", e
else:
	print "Written content in the file successfully" 
	fh.close()

print "selesai!"
