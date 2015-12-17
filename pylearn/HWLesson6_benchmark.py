# coding=utf-8

import random
import datetime
import HWLesson6_BluePrint as makemagick

def bubble_sort(list_):
    list_bub = list_[:]
    len_list = len(list_bub)
    for i in range(len_list - 1):
        for j in range(len_list - i - 1):
            if list_bub[j] > list_bub[j + 1]:
                bub = list_bub[j]
                list_bub[j] = list_bub[j + 1]
                list_bub[j + 1] = bub
    return(list_bub)

def py_sort(list_):
    list_py = list_[:]
    list_py.sort()
    return(list_py)

def avarage_time(list_):
    av_list = list_[:]
#    print('DEBUG: Original av_list {}'.format(av_list))
    av_list.remove(min(av_list))
    av_list.remove(max(av_list))
#    print('DEBUG: Removed min/max av_list {}'.format(av_list))
    av_out = sum(av_list) / len(av_list)
    return(av_out)


if __name__ == '__main__':
    for i in range(0, 10000, 1000):
        list_ = range(i)
        random.shuffle(list_)

        start_copy_list = datetime.datetime.now()
        copy_list = list_[:]
        finish_copy_list = datetime.datetime.now()
        t_copy = (finish_copy_list - start_copy_list).total_seconds()

        t_bubble_sort = []
        t_py_sort = []
        ''' Minimum 5 experiments for each range. Each sort_time placed in the list'''
        for j in range(0, 8):
            start_bubble_sort = datetime.datetime.now()
            bubble_sort(list_)
            finish_bubble_sort = datetime.datetime.now()
            t = (finish_bubble_sort - start_bubble_sort).total_seconds() - t_copy
            t_bubble_sort.append(t)

            start_py_sort = datetime.datetime.now()
            py_sort(list_)
            finish_py_sort = datetime.datetime.now()
            t = (finish_py_sort - start_py_sort).total_seconds() - t_copy
            t_py_sort.append(t)
#        print('DEBUG: Avarage time bubble {}'.format(avarage_time(t_bubble_sort)))
#        print('DEBUG: Avarage time py {}'.format(avarage_time(t_py_sort)))
        list_ = []

        with open('time_sort.txt', 'a+') as file:
            file.write('{}, {}, {}\n'.format(i, avarage_time(t_bubble_sort), avarage_time(t_py_sort)))

#    makemagick.two_benchmarks_graph()