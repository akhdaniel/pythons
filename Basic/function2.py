def changeme( mylist ):
	mylist.append([11,22,33])
	print "my list di dalam function: ", mylist
	return

mylist = [2,3,4]
print "my list sebelum function: ", mylist
changeme(mylist)
print "my list di luar function: ", mylist
