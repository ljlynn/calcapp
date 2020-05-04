'''
Pytest unit testing code for the calculator service. 
'''

import pytest
import calculator

def test_add_two_numbers():
    '''
    Test method for the add_numbers function.
    '''
    calc_obj1 = calculator.Calculator(2, 2)
    assert calc_obj1.add_numbers() == 4
    calc_obj2 = calculator.Calculator(1, -1)
    assert calc_obj2.add_numbers() == 0

def test_return_json():
    calc_obj3 = calculator.Calculator(2, 2)
    json_obj = calc_obj3.return_json()

    assert json_obj['sum'] == 4