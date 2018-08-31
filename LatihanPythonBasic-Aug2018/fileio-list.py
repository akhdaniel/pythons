

# open file
fo = open("data.txt", "rb+")
content = fo.read()
data = content.split("\n")

# print data
output = []
for name in data:
	output.append("Name %s" % name)

# close
fo.close()


# data = "\n".join(output)


data = ""
for name in output:
	data += name + "\n"

fo = open("data3.txt", "wb+")
fo.write(data)
fo.close()

