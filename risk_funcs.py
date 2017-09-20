import numpy as np
from random import randint

def single_roll(n_atk, n_def):

    # assert correct inputs
    assert n_atk in [1,2,3]
    assert n_def in [1,2]

    # roll for attacker and defender
    get_roll = lambda n: np.sort([randint(1,6) for _ in range(n)])[::-1]
    atk_roll = get_roll(n_atk)
    def_roll = get_roll(n_def)

    # print results
    result = [True if x > 0 else False for x in atk_roll[:n_def] - def_roll]
    print('Attacker rolls {} and defender rolls {};'.format(atk_roll, def_roll), end=' ')
    if (len(result) > 1) and (sum(result) == 1):
        return print("both lose one unit")
    elif all(result):
        return print("the defender loses {} unit(s).".format(len(result)))
    return print("the attacker loses {} unit(s).".format(len(result)))

def battle_sim(n_atk_unit, n_def_unit):

    # assert correct inputs
    assert n_atk_unit > 1
    assert n_def_unit > 0

	# define dice roll function
    get_roll = lambda n: np.sort([randint(1,6) for _ in range(n)])[::-1]

    # start battle
    while True:

    	# set n dice for atk and def
        n_atk = min(n_atk_unit - 1, 3)
        n_def = min(n_def_unit, 2)

        # get results
        res = [True if x > 0 else False for x in get_roll(n_atk)[:n_def] - get_roll(n_def)]

        # update units
        if (len(res) > 1) and (sum(res) == 1):
            n_atk_unit -= 1
            n_def_unit -= 1
        elif all(res):
            n_def_unit -= 2
        else:
            n_atk_unit -= 2

        # return winner and remaining units
        if n_atk_unit < 2:
            return print('Defender wins: {} units remaining.'.format(n_def_unit))
        elif n_def_unit < 1:
            return print('Attacker wins: {}+1 units remaining'.format(n_atk_unit - 1))
