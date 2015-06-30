__author__ = 'cloudera'


def recursive_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + recursive_sum(num_list[1:])

print recursive_sum([1, 2, 3, 4, 5])
