import random

"""
Python3 supports custom list(container?) 
"""

class CustomContainer(object):
    def __init__(self, num):
        self.num = num
        self.size = 0
        self.point = 0
        self.data = list()
        for i in range(self.num):
            self.data.append(random.randint(0,10))
        self.size = len(self.data)


    def __iter__(self):
        """
        This function is called in for x in iterable
        //////
        for i in range(self.num):
            self.data.append(random.randint(0,10))
        self.size = len(self.data)
        """
        return self

    def __next__(self):
        """
        This funcion is called in the for statement.
        """
        if self.point < self.size:
            value = self.data[self.point]
            self.point += 1
            return value
        else:
            raise StopIteration


if __name__ == '__main__':

    test_list = CustomContainer(100)

    for rnd_num in test_list:
        print(str(rnd_num) + ' ',end='')