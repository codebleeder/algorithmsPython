__author__ = 'cloudera'


def nth_to_last(head, k):
    if head is None:
        return 0
    i = nth_to_last(head.get_next(), k)
    if i == k:
        print head.get_data()
    return i
