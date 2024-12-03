# employees.txt

def main():
	on = True
	while on == True:
		input_file = input("Please enter a file name: ")
		record_search2(input_file)
		end_program = input("Continue y/n: ")
		if end_program == 'n':
			on = False
		print()

def record_search2(file):
	try:
		term = input("Enter a name to search for: ")
		f = open(file, 'r')
		found = False
		content = f.read()
		try:
			if term not in content:
				raise Exception(f"'{term}' not found in the file.")
			if term in content:
				print(f"'{term}' is in the file.")
		except ValueError:
			print("A value is wrong in the program")
		finally:
			f.close()
	except IsADirectoryError:
		print(f"[Errno1] file is a directory: '{file}'")
		print("The file has been closed.")
	except FileNotFoundError:
		print(f"[Errno2] no such file or directory: '{file}'")
		print("The file has been closed.")

main()
