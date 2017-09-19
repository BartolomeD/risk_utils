import numpy as np
from random import sample

# define function to perform n dice rolls
def roll_sim(n):
	return np.sort(sample(range(1, 7), n))[::-1]

# this function returns custom outcome
def on_outcome(res, atk_win, def_win, draw):
	if (len(res) > 1) and (sum(res) == 1):
		return draw
	elif all(res):
		return atk_win
	return def_win

# this function rolls dice and subtracts losses from army size
def roll_apply(n_atk_unit, n_def_unit):
	n_atk = min(n_atk_unit - 1, 3)
	n_def = min(n_def_unit, 2)
	res = [True if x > 0 else False for x in roll_sim(n_atk)[:n_def] - roll_sim(n_def)]
	return on_outcome(res, (n_atk_unit - 1, n_def_unit - 1),
						   (n_atk_unit, n_def_unit - len(res)),
						   (n_atk_unit - len(res), n_def_unit))

# this function returns the result of a single roll
def roll_result(n_atk, n_def):
	atk_roll = roll_sim(n_atk)
	def_roll = roll_sim(n_def)
	res = [True if x > 0 else False for x in atk_roll[:n_def] - def_roll]
	print('Attacker rolls {} and defender rolls {};'.format(atk_roll, def_roll), end=' ')
	return on_outcome(res, 'the defender loses {} unit(s).'.format(len(res)),
						   'the attacker loses {} unit(s).'.format(len(res)),
						   'both lose 1 unit.')

# this function returns the result of an entire battle
def battle_result(n_atk_unit, n_def_unit):
	while True:
		n_atk_unit, n_def_unit = roll_apply(n_atk_unit, n_def_unit)
		if n_atk_unit < 2:
			return print('Defender wins: {} units remaining.'.format(n_def_unit))
		elif n_def_unit < 1:
			return print('Attacker wins: {}+1 units remaining'.format(n_atk_unit - 1))
