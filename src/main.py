#!/usr/bin/python3 
import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(name)s %(levelname)s %(message)s')

logger=logging.getLogger('DataCapture')

class DataCapture():

    def __init__(self):
        self.numbers = []

    def add(self,num):
        if type(num) == int:
            self.numbers.append(num)

    def get_collection(self):
        return self.numbers

    def build_stats(self):
        return Stats(self.numbers)

class Stats():

    def __init__(self,numbers):
        self.numbers = numbers

    def less(self,num):
        amount = len([i for i in self.numbers if i < num])
        #amount = 0
        #for i in self.numbers:
        #    if i < num:
        #        amount += 1
        logger.debug('The amount of values less than <%s> is <%s>' % (str(num),str(amount)))
        return amount

    def between(self,num_1,num_2):
        amount = len([i for i in self.numbers if num_1 <= i <= num_2])
        #amount = 0
        #for i in self.numbers:
        #    if num_1 <= i <= num_2:
        #        amount += 1
        logger.debug('The amount of values between the numbers <%s> and <%s> is <%s>' % (str(num_1),str(num_2),str(amount)))
        return amount

    def greater(self,num):
        amount = len([i for i in self.numbers if i > num])
        #amount = 0
        #for i in self.numbers:
        #    if i > num:
        #        amount += 1
        logger.debug('The amount of values greater than <%s> is <%s>' % (str(num),str(amount)))
        return amount

if __name__ == "__main__":

    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()

    print(capture)
    #print(capture.numbers)

    print(stats.less(4))
    print(stats.between(3,6))
    print(stats.greater(4))
