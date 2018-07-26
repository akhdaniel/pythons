fo = open("data.txt", "r+")
str = fo.read(10)
print "isi file: ", str 

position = fo.tell();
print "Current file position : ", position

str = fo.read(10)
print "next 10 char: ", str 

position = fo.tell();
print "Current file position : ", position

position = fo.seek(0);
str = fo.read(10)
print "char: ", str 


fo.close()
