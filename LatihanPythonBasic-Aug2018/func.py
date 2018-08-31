def print_name(name, age, email="default@email.com", *tambahan):
	print name.center(80,"-")
	print age.center(80," ")
	print email.center(80," ")
	for arg in tambahan:
		print arg 
	print "-" * 80
	print "\n"




print_name( "dodo", "90", "email" )
print_name( "dodo", "90", "email", 20 )
print_name( "dodo", "90", "email", 20, 30, 20, 30 )



db = """def printx():
	print 'data adalah...'
"""

eval(db)
