#! /home/myke/anaconda3/bin/python3.7
import load_balancer

assert load_balancer.read_input_file('input.txt') == [1, 3, 0, 1, 0, 1], f'Fail on read_input_file.'

assert load_balancer.simulation(4, 2, [1, 3, 0, 1, 0, 1]) == [[[4]],
															[[3, 4], [4, 4]],
															[[2, 3], [3, 3]],
															[[1, 2], [2, 2], [4]],
															[[1], [1, 1], [3]],
															[[2, 4]],
															[[1, 3]],
															[[2]],
															[[1]],
															[]], f'Fail on simulation.'

print('Test Ok.')
