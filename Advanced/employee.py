class Employee:
	empCount = 0

	def __init__(self, name, salary):
		self.name = name 
		self.salary = salary
		Employee.empCount += 1 

	def displayCount(self):
		print "Total employee %d" % Employee.empCount

	def displayEmployee(self):
		print "Name: ", self.name 
		print "Salary: ", self.salary


emp1 = Employee("Zara", 2000)
emp2 = Employee("Joko", 3000)
emp3 = Employee("Adi", 4000)

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()

emp1.age = 10



print emp1.age
print getattr(emp1, 'age')

emp1.age = 8
setattr(emp1, 'age', 8)
print emp1.age


delattr(emp1, 'age')


print "Total Employee: %d" % Employee.empCount
