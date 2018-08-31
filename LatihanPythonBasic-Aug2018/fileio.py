

print "hallo python"
data = raw_input("\n\nMasukkan pilihan anda:")
print "pilihan anda adalah %s" % data 



# open file
fo = open("data.txt", "r")
print "Nama file:", fo.name

# read

content = fo.read(10)

print "Isi file:"
print content


# close
fo.close()
