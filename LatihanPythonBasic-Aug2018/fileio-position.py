

# open file
fo = open("data.txt", "r")

# read
content = fo.read(10)
print "Isi file 10 bytes pertama:"
print content
position = fo.tell()
print "Posisi saat ini %s" % position


fo.seek(50)
content = fo.read(10)
print "Isi file 10 bytes berikutnya:"
print content
position = fo.tell()
print "Posisi saat ini %s" % position


fo2 = open("data4.txt", "wb+")
fo2.write(content)


# close
fo.close()
fo2.close()
