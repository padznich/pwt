# coding=utf-8

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str, required=True, help='Enter path to file.')
parser.add_argument('--set_mode', type=str, default='union', help='Enter path to set mode.')
args = parser.parse_args()

file = args.file
set_mode = args.set_mode

with open(file, 'r') as file:
    slist = file.readlines()
s1 = set((slist[0]).split())
s2 = set((slist[1]).split())
out = 's1.{}(s2)'.format(set_mode)
out = eval(out)

print(out)