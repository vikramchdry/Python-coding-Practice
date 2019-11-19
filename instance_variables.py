class Student:
	def __init__(self , rollno, name):
		self.rollno = rollno
		self.name = name

	def info(self):
		self.marks = 60
		x =10



s = Student(101, 'vikram')
s.info()
print(s.__dict__)






