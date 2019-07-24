from sys import exit

input_file_address = 'input.txt'
output_file_address = 'output.txt'
Ttask = 4
Umax = 2

BOLD = '\033[1m'
END = END = '\033[0m'

print(f'Reading {BOLD}{input_file_address}{END}...')
new_users = []
with open(input_file_address, 'r') as input_file:
	for row in input_file:
		try:
			new_users.append(int(row))
		except ValueError as e:
			print(f'{BOLD}ERROR:{END} Invalid value in {BOLD}{input_file_address}{END}')
			exit(1)

print(new_users)