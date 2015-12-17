# coding=utf-8

import matplotlib.pyplot as plt

def two_benchmarks_graph():
    t_list_bub = []
    t_list_py = []
    range_list = []
    with open('time_sort.txt', 'r') as file:
        if file.mode == 'r':
            for line in file:
                line = line.split(',')
                range_list.append(line[0])
                t_list_bub.append(line[1])
                t_list_py.append(line[2][:-1])

    x = range_list
    y1 = t_list_bub
    y2 = t_list_py

    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.xlabel('Range of input list')
    plt.ylabel('time, [sec]')
    plt.show()

    return False

if __name__ == '__main__':
    two_benchmarks_graph()