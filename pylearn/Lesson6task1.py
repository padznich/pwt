# coding=utf-8

import datetime

def binary_search(list_, value):
    """This function performs a binary search.
    """
    first = 0
    last = len(list_) - 1

    while first <= last:
        middle = first + (last - first) // 2
        if value == list_[middle]:
            return middle
        elif value < list_[middle]:
            last = middle - 1
        else:
            first = middle + 1

    return None


def linear_search(list_, value):

    for i, item in enumerate(list_):
        if item == value:
            return i

    return None


if __name__ == "__main__":
    for i in range(2, 7):
        value = 10 ** i - 1
        list_ = range(10 ** i)

        start_b = datetime.datetime.now()
        binary_search(list_, value)
        finish_b = datetime.datetime.now()
        t_binary = finish_b - start_b

        start_l = datetime.datetime.now()
        linear_search(list_, value)
        finish_l = datetime.datetime.now()
        t_linear = finish_l - start_l

        print('_' * 100)
        print(r'For list = range({:8}) | Binary search is: {:10}  | Linear search is: {}'.format
              (10 ** i, t_binary, t_linear))
    print('_' * 100)