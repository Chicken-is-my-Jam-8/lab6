# only able to calculate ineger values at the moment
# numbers.txt
def main():
	on = True
	print("Welcome to the total sum program")
	print("Please enter a file full of numbers to calculate a total from")
	print()
	while on == True:
		file = input("Please enter a file name: ")
		list_string = create_list_string(file)
		total = calculate_total(file)
		print(f"The numbers are: {list_string}")
		print(f"Their total is: {total}")
		end_program = input("Continue y/n: ")
		if end_program == 'n':
			on = False

def create_list_string(data):
	try:
		f = open(data, 'r')
		s = f.read()
		f_string = ''
		try:
			for x in s:
				if x.isdigit() == True:
					f_string = f_string + x
				elif x.isdigit() == False:
					f_string = f_string + ", "
				f_string.rstrip(", ")
			return f_string
		except ZeroDivisionError:
			print("ZeroDivisionError: use a file with integer values")
		except:
			print("Something went wrong")
		finally:
			f.close()
	except FileNotFoundError:
		print("Invalid file name")



def calculate_total(data):
	try:
		total = 0
		f = open(data, 'r')
		s = f.read()
		f_string = ''
		try:
			for x in s:
				if x.isdigit() == True:
					f_string = f_string + x
				elif x.isdigit() == False:
					total += int(f_string)
					f_string = ''
			return total
		except ZeroDivisionError:
			print("ZeroDivisionError: use a file with integer values")
		except:
			print("Something went wrong")
		finally:
			f.close()
	except FileNotFoundError:
		print("Invalid file name")

main()
