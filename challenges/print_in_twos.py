__author__ = 'cloudera'
from math import ceil
from sys import stdout


def print_in_twos(arr):
    rows = int(ceil(float(len(arr))/2.0))
    index = 0
    for row in range(rows):
        for col in range(2):
            if index < len(arr):
                stdout.write(str(arr[index]))
                index += 1
        print " "
print_in_twos([1,2,3,4,5])
