# employees.txt
def main():
	on = True
	file = input("Please enter a file name: ")
	while on == True:
		search_term = input("Enter a name to search for: ")
		lines = count_lines(file)
		record_search(search_term, file, lines)
		end_program = input("Continue y/n: ")
		if end_program == 'n':
			on = False
		print()

def record_search(term, input_file, line_num):
	f = open(input_file, 'r')
	found = False
	for x in range(line_num):
		name = f.readline()
		id_num = f.readline()
		department = f.readline()
		n = name.rstrip()
		if n == term:
			found = True
			print(f"Name: {name}")
			print(f"Name: {id_num}")
			print(f"Name: {department}")
	f.close()
	if found == False:
		print("That record was not found in the file.")

def count_lines(input_file):
	f = open(input_file, 'r')
	no_str = False
	count = 0
	s = f.read()
	for x in s:
		if x == '\n':
			count += 1
	if x != '\n':
		count += 1
	f.close
	return count

main()
