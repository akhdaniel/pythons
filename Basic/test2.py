#!/usr/bin/python
import sys

try:
	# open file stream
	file = open(file_name, "w")
except IOError:
	print "There was an error writing to", file_name
	sys.exit()

print "Enter '", file_finish, 
print "' When finished"

while file_text != file_finish:
	file_text = raw_input("Enter text: ") 
	if file_text == file_finish:
		# close the file
		file.close
		break

	file.write(file_text)
	file.write("\n")

file.close()
file_name = raw_input("Enter filename: ") 
if len(file_name) == 0:
	print "Next time please enter something"
	sys.exit() 

try:
	file = open(file_name, "r") 
except IOError:
	print "There was an error reading file"
	sys.exit()

file_text = file.read() 
file.close()
print file_text
                 




total = item1 + \
item2 + \
item3



# array list
days = ['Monday', 'Tuesday', 'Wednesday', 
			'Thursday', 
			'Friday'] 

# dictionary
days = {'Monday', 
			'Tuesday', 
			'Wednesday', 
			'Thursday', 
			'Friday'}

# nama = 'python training'
nama = "python training" # nama training
nama = '''python training
jdfjklsdjfklj
jfdjfklds jfkla
jsdfkjdslfj kfsjklfj sldkjfl
fkdsjlkfjsklf jfdskfj lskd
fkljdskjfsld
jfksdjflks jj fkjdlkg
jfkdsjfls
fksdjfkljs'''











'''
sdjklsjf jsdfjlsd
jflksdjfls jdfk
jfldjsalfjsdklf
jsldakjfklds jflk
'''

print "fjjjjj"





