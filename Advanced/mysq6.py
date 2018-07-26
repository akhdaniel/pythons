import mysql.connector

# open connection
cnx = mysql.connector.connect(user='root', 
								password='1234',
                              	host='127.0.0.1',
                              	database='pythondb')

cursor = cnx.cursor()

# data input:
data = [
	{'first_name':'ade', 'last_name':'dodi','age':20,'income':4000,'sex':'M'},
	{'first_name':'ayu', 'last_name':'dodi','age':40,'income':4000,'sex':'M'},
	{'first_name':'adi', 'last_name':'dodi','age':50,'income':4000,'sex':'M'},
	{'first_name':'dodo', 'last_name':'dodi','age':30,'income':4000,'sex':'M'},
	{'first_name':'edi', 'last_name':'dodi','age':24,'income':4000,'sex':'M'},
]

# 2. insert record
sql = """INSERT INTO EMPLOYEE(
	FIRST_NAME, 
	LAST_NAME, 
	AGE, 
	SEX, 
	INCOME)
VALUES (
	'%s', 
	'%s', 
	%d, 
	'%s', 
	%d)"""

try:
	for rec in data:
		cursor.execute(sql % (
				rec['first_name'],
				rec['last_name'],
				rec['age'],
				rec['sex'],
				rec['income'],
			))

	cnx.commit()
	print "statement commmit"
except Exception, e:
	print "Error: ", e	
	print "statement rollback"
	cnx.rollback()


# close connection
cnx.close()
