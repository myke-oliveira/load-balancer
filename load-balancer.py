#! /home/myke/anaconda3/bin/python3.7
from sys import exit

input_file_address  = 'input.txt'
output_file_address = 'output.txt'

Ttask = 4
Umax  = 2

BOLD = '\033[1m'
END  = '\033[0m'

print(f'Reading {BOLD}{input_file_address}{END}...')
new_users_per_tick = []
with open(input_file_address, 'r') as input_file:
	for row in input_file:
		try:
			new_users_per_tick.append(int(row))
		except ValueError:
			print(f'{BOLD}ERROR:{END} Invalid value in {BOLD}{input_file_address}{END}')
			exit(1)
print('Reading done.')

print('Starting the Simulation...')
t = 0
servers_per_tick = []
servers = []
while True:
	try:
		new_users = new_users_per_tick[t]
	except IndexError:
		new_users = 0
	
	if new_users == 0 and len(servers) == 0:
		break

	print(f't: {t}')

	# Um tick a menos em cada tarefa
	servers = [list(map(lambda x: x - 1, server)) for server in servers]

	# Desalocando tarefas finalizadas
	for server in servers:
		while 0 in server:
			server.remove(0)

	# Desalocando servidores ociosos
	while [] in servers:
		servers.remove([])

	# Alocando cada usuário novo
	while new_users > 0:
		if len(servers) == 0 or all(len(server) == Umax for server in servers):
			servers.append([Ttask])
		else:
			server_available = list(filter(lambda server: len(server) < Umax, servers))[0]
			server_available.append(Ttask)
		new_users -= 1

	print(f'Servers Status: {servers}')
	print(*(len(server) for server in servers), sep=',')
	servers_per_tick.append(servers)
	t += 1
print('Simulation done.')

print(f'Saving results into {BOLD}{output_file_address}{END}...')
with open(output_file_address, 'w') as output_file:
	for tick in servers_per_tick:
		output_file.write(','.join(str(len(server)) for server in tick))
		output_file.write('\n')
print('Results Saved.')
