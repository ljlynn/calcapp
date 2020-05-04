'''
This module provides the calculator service. 
'''

class Calculator():
    '''
    Class object for the calculator service
    '''
    
    def __init__(self, first_number, second_number):
        '''
        Constructor for the Calculator service. Numbers used by calulator are stored here.
        '''
        self.first_number = int(first_number)
        self.second_number = int(second_number)

    def add_numbers(self):
        '''
        This method takes two numbers and adds them together.
        '''
        return self.first_number + self.second_number

    def return_json(self):
        obj_sum = self.add_numbers()
        return {
            'first_number': self.first_number,
            'second_number': self.second_number,
            'sum': obj_sum
        }
