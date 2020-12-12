import csv
class local_database():
	def __init__(self,filename):
		self.filename=filename
		self.data= ['First Name','Last Name','Roll Number','Section','Phone Number']
		self.insert_data()
	def get_data(self):
		self.data=list(map(str,input('Enter The values: ').split()))
	def insert_data(self):
		with open(self.filename,'a',newline='') as csvfile:
			csvwriter= csv.writer(csvfile,delimiter=',')
			csvwriter.writerow(self.data)
	def display_data(self):
		with open(self.filename,'r') as csvfile:
			csvreader=csv.reader(csvfile,delimiter=',')
			for i in csvreader:
				print(i)
	def write_data(self):
		ch='y'
		while ch=='y':
			self.get_data()
			self.insert_data()
			ch=input('Want to Enter more rows (Y/n):')

if __name__ == '__main__':
	obj = local_database("database.csv")
	ch1='y'
	while ch1=='y':
		print('''
			Choose one option :
			1. Enter Data into database
			2. Display Data
			3. Close Program''')
		inp=input('Enter your choice : ')
		if inp =='1' :
			obj.write_data()
			for i in range(50):
				print("*",end='')
		else:
			if inp =='2':
				obj.display_data()
				for i in range(50):
					print("*",end='')
			else:
				if inp=='3':
					ch1='n'
	