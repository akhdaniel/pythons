

data = ['andi','budi','joni', 123, 456, 6970.0]

data[3]=100
print data[3]


del data[2]


data[-3]


count = 0
for x in data:
	if x=='motor':
		count +=1

print count




print len(data)

data.append()




data_tuple = ('draft','open','closed')

print data_tuple[2]
print data_tuple[2:]
print data_tuple[-2:]

tuple2 = ('baru',) + data_tuple[-2:]




t5 = (
	(8,9,0),
	(3,4,5),
	(2,3,4),
	(1,2,3),
	[2,3,4]
)



user1 = {'name' : 'andi',
		 'age'    : 20,
		 'email'  : 'andi@andi.com'
	    }

print user1['name']
print user1['age']
print user1['email']


data = [
	[1,2,3,4],
	[4,5,6,7],
	[4,5,4,3],
	[1,2,5,6],
]

data[2][2]
data[3][3]




records = [
	{'nik': 11223, 'name':'dodo'},
	{'nik': 11211, 'name':'didi'},
	{'nik': 11277, 'name':'dede'},
]


records[2]['name']














