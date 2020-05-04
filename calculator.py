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
        self.first_number = first_number
        self.second_number = second_number

    def add_numbers(self):
        '''
        This method takes two numbers and adds them together.
        '''
        return self.first_number + self.second_number
