#!/usr/bin/python
import sys
import numpy as np
from random import sample

def roll_result(n_atk, n_def):
    
    # define function to perform dice roll
    simulate_roll = lambda x: np.sort(sample(range(1, 7), x))[::-1]
    
    # roll dice for attacker and defender
    atk_roll = simulate_roll(n_atk)
    def_roll = simulate_roll(n_def)
    
    # calculate winning rolls
    dif = [True if x > 0 else False for x in atk_roll[:n_def] - def_roll]
    
    # print roll results
    print('Attacker rolls {} and defender rolls {};'.format(atk_roll, def_roll), end=' ')
    if (len(dif) > 1) and (sum(dif) == 1):
        return print('both lose 1 unit.')
    if all(dif):
        return print('the defender loses {} unit(s).'.format(len(dif)))
    return print('the attacker loses {} unit(s).'.format(len(dif)))

if __name__ == '__main__':
    roll_result(int(sys.argv[1]), int(sys.argv[2]))
