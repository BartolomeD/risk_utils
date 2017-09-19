#!/usr/bin/python
import numpy as np
from random import sample

# define function to perform n dice rolls
roll_sim = lambda n: np.sort(sample(range(1, 7), n))[::-1]

# this function returns the result of a single roll
def roll_result(n_atk, n_def):
    
    # roll dice for attacker and defender
    atk_roll = roll_sim(n_atk)
    def_roll = roll_sim(n_def)
    
    # calculate winning rolls
    res = [True if x > 0 else False for x in atk_roll[:n_def] - def_roll]
    
    # print roll results
    print('Attacker rolls {} and defender rolls {};'.format(atk_roll, def_roll), end=' ')
    if (len(res) > 1) and (sum(res) == 1):
        return print('both lose 1 unit.')
    if all(res):
        return print('the defender loses {} unit(s).'.format(len(res)))
    return print('the attacker loses {} unit(s).'.format(len(res)))

# this function returns the result of an entire battle
def battle_result(n_atk_unit, n_def_unit):

    def roll_apply(n_atk, n_def):

        # roll
        x = [True if x > 0 else False for x in roll_sim(n_atk)[:n_def] - roll_sim(n_def)]

        # apply
        if len(x) > 1 and sum(x) == 1:
            return n_atk_unit - 1, n_def_unit - 1
        elif all(x):
            return n_atk_unit, n_def_unit - len(x)
        else:
            return n_atk_unit - len(x), n_def_unit

    # start battle
    while True:

        # get and apply roll results
        n_atk_unit, n_def_unit = roll_apply(min(n_atk_unit - 1, 3), min(n_def_unit, 2))

        # check for finish
        if n_atk_unit < 2:
            return 'Defender wins: {} units remaining.'.format(n_def_unit)
        elif n_def_unit < 1:
            return 'Attacker wins: {}+1 units remaining'.format(n_atk_unit - 1)
