# only able to calculate ineger values at the moment
#linear_nums.txt
#2d.csv
def main():
	on = True
	print("Welcome to the averaging program")
	print("Please enter a file full of numbers to calculate an average from")
	print()
	while on == True:
		file = input("Please enter a file name: ")
		average = calculate_average(file)
		print(average)
		end_program = input("Continue y/n: ")
		if end_program == 'n':
			on = False

def calculate_average(data):
	try:
		count = 0
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
					count += 1
					f_string = ''
			average = total / count
			return average
		except ZeroDivisionError:
			print("ZeroDivisionError: use a file with integer values")
		except:
			print("Something went wrong")
		finally:
			f.close()
	except FileNotFoundError:
		print("Invalid file name")

main()
