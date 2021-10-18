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

    def build_stats(self):

        '''Build two dicts with the less and greater values found between the min and max item of the collection '''

        self.numbers.sort()
        total_list_size = len(self.numbers)
        for i in range(self._get_max_item_value(self.numbers)+1):
            next_greater, next_less = self._get_next_values(i)
            logger.debug('next_greater <%s> of iterator <%s>' % (str(next_greater),str(i)))
            logger.debug('next_less <%s> of iterator <%s>' % (str(next_less),str(i)))

            if i not in self.less_values and next_less:
                self.less_values[i] = len(self.numbers[0:self._get_max_item_index(next_less)])
            elif i not in self.less_values:
                self.less_values[i] = 0

            if i not in self.greater_values and next_greater:
                self.greater_values[i] = total_list_size - len(self.numbers[0:self._get_max_item_index(next_greater)])
            elif i not in self.greater_values:
                self.greater_values[i] = total_list_size
        
        logger.debug('self.less_values: %s' % self.less_values)
        logger.debug('self.greater_values: %s' % self.greater_values)
        self.numbers.clear()
        return Stats(self.numbers, self.less_values, self.greater_values)

    def _get_max_item_value(self,numbers):
        
        '''Internal method to get the max value of te collection (must be sorted from high to low)'''
        return numbers[len(numbers)-1]

    def _get_max_item_index(self, i):
        
        '''Internal method to get the max value of the collection'''

        return len(self.numbers) - self.numbers[::-1].index(i)

    def _get_next_values(self, i):

        '''Internal method to get the less and greater value of an iterator i from the collection of numbers'''

        logger.debug('_get_next_values, i: %s' % i)
        greater = 0
        less = 0
        less_already_set = False
        greater_already_set = False
        for n in self.numbers[::-1]:
            logger.debug('_get_next_values, n: %s' % n)
            if i > n and not less_already_set:
                logger.debug('_get_next_values, found a less value: <%s>' % n)
                less = n
                less_already_set = True
            if i >= n and not greater_already_set:
                logger.debug('_get_next_values, found a greater value: <%s>' % n)
                greater = n
                greater_already_set = True
        return greater, less

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

    def _between(self, num_1, num_2):

        ''' Method not working'''

        if not(type(num) == int):
            return 0
        if num_1 > num_2:
            return 0
        greater = self.greater(num_1)
        less = self.less(num_2)

        return greater - less

    def between(self,num_1,num_2):

        if not(type(num) == int):
            return 0
        if num_1 > num_2:
            return 0
        amount = len([i for i in self.numbers if num_1 <= i <= num_2])
        logger.debug('The amount of values between the numbers <%s> and <%s> is <%s>' % (str(num_1),str(num_2),str(amount)))
        return amount

    def greater(self,num):

        if not(type(num) == int):
            return 0
        amount = len([i for i in self.numbers if i > num])
        logger.debug('The amount of values greater than <%s> is <%s>' % (str(num),str(amount)))
        return amount

