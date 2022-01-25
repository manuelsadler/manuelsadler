class Employee:
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		self.email=first + '.' +last+ '@company.com'


	def fullname(self):
		return '{} {} '.format(self.first,self.last)


class Animal:
	def __init__(self,rasse,gattung,name):
		self.rasse=rasse
		self.gattung=gattung
		self.name=name


	def Tier(self):
		return '{} {} '.format(self.name,self.rasse)



emp_1=Employee('Manuel','Sadler',40000)


tier1=Animal('Hund','Saeugetier','Hunter')


print(tier1.Tier())