import re
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="specify word to search for")
    parser.add_argument("fname", help="specify file to search")
    args = parser.parse_args()

    with open(args.fname) as file:

        line_num = 0
        for line in file.readlines():
            line = line.strip('\n\r')
            line_num += 1

            search_result = re.search(args.word, line, re.M|re.I)

            if search_result:
                print(str(line_num) + ": " + line)

def compile_search(pattern, sstring):
    '''
    When using the same pattern multiple times in loop.
    Program more efficient by compiling.
    :param pattern:
    :param sstring:
    :return:
    '''
    my_re = re.compile(pattern)
    result = my_re.search(sstring)

if __name__ == '__main__':
    main()