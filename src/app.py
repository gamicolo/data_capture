#!/usr/bin/python3 
import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(name)s %(levelname)s %(message)s')

logger=logging.getLogger('DataCapture')

class DataCapture():

    def __init__(self):

        self.numbers = []
        self.less_values = {}
        self.greater_values = {}

    def add(self,num):

        if type(num) == int:
            self.numbers.append(num)

    def get_numbers(self):

        return self.numbers

    def build_stats(self):

        '''Build two dicts with the less and greater values found between the min and max item of the collection '''

        self.numbers.sort()
        total_list_size = len(self.numbers)
        for i in range(self._get_max_value(self.numbers)+1):
            next_less_equal, next_less_strict = self._get_less_values(i)

            if i not in self.less_values and next_less_strict:
                self.less_values[i] = len(self.numbers[0:self._get_max_index(next_less_strict)])
            elif i not in self.less_values:
                self.less_values[i] = 0

            if i not in self.greater_values and next_less_equal:
                self.greater_values[i] = total_list_size - len(self.numbers[0:self._get_max_index(next_less_equal)])
            elif i not in self.greater_values:
                self.greater_values[i] = total_list_size
        
        logger.debug('self.less_values: %s' % self.less_values)
        logger.debug('self.greater_values: %s' % self.greater_values)
        self.numbers.clear()
        return Stats(self.numbers, self.less_values, self.greater_values)

    def _get_max_value(self,numbers):
        
        '''Internal method to get the max value of a sorted (from high to low) list of numbers'''

        return numbers[len(numbers)-1]

    def _get_max_index(self, i):
        
        '''Internal method to get the max index of a sorted (from high to low) list of numbers'''

        return len(self.numbers) - self.numbers[::-1].index(i)

    def _get_less_values(self, i):

        '''Internal method to get the less and less equal values of a list'''

        logger.debug('_get_less_values, i: %s' % i)
        less_equal = 0
        less_strict = 0
        less_equal_already_set = False
        less_strict_already_set = False
        for n in self.numbers[::-1]:
            logger.debug('_get_less_values, n: %s' % n)
            if i > n and not less_strict_already_set:
                logger.debug('_get_less_values, found a less strict value: <%s>' % n)
                less_strict = n
                less_strict_already_set = True
            if i >= n and not less_equal_already_set:
                logger.debug('_get_less_values, found a less equal value: <%s>' % n)
                less_equal = n
                less_equal_already_set = True
        logger.debug('less equal value of iterator <%s> is <%s>' % (str(i), str(less_equal)))
        logger.debug('less strict value of iterator <%s> is <%s>' % (str(i),str(less_strict)))
        return less_equal, less_strict

class Stats():

    def __init__(self,numbers,less_values, greater_values):

        self.numbers = numbers
        self.max_less_value = len(numbers)
        self.less_values = less_values
        self.greater_values = greater_values

    def less(self,num):

        if not(type(num) == int):
            return 0
        amount = self.less_values.get(num)
        if amount == None:
            amount = self.max_less_value
        logger.debug('The amount of values less than <%s> is <%s>' % (str(num),str(amount)))
        return amount

    def between(self,num_1,num_2):

        if not(type(num_1) == int) or not(type(num_2) == int):
            return 0
        if num_1 > num_2:
            return 0
        amount = len([i for i in self.numbers if num_1 <= i <= num_2])
        logger.debug('The amount of values between the numbers <%s> and <%s> is <%s>' % (str(num_1),str(num_2),str(amount)))
        return amount

    def _greater(self,num):

        if not(type(num) == int):
            return 0
        amount = len([i for i in self.numbers if i > num])
        logger.debug('The amount of values greater than <%s> is <%s>' % (str(num),str(amount)))
        return amount

    def greater(self,num):

        if not(type(num) == int):
            return 0
        amount = self.greater_values.get(num)
        if amount == None:
            amount = 0
        logger.debug('The amount of values greater than <%s> is <%s>' % (str(num),str(amount)))
        return amount
