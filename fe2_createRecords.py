# employees.txt
def main():
	file = input("Please enter a file name: ")
	f = open(file, 'a')
	record_num = int(input("How many employee records do you want to create? "))
	for x in range(record_num):
		print(f"Enter data for employee #{x + 1}")
		name = input("Name: ")
		id_num = input("ID number: ")
		department = input("Department: ")
		f.write(name + "\n")
		f.write(id_num + "\n")
		f.write(department + "\n")
		print()
	f.close()
	print(f"Employee records writen to {file}")
main()
