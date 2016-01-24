import argparse
# https://pymotw.com/2/argparse/
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def main():
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quite", action="store_true")

    parser.add_argument("num", type=int, help="The fibonacci numbers")
    parser.add_argument("-o", "--output", help="Output result to a file.",
                        action="store_true")
    args = parser.parse_args()

    result = fib(args.num)
    if args.verbose:
        print("The " + str(args.num) + "th fib number is " + str(result))
    elif args.quite:
        print(result)
    else:
        print("Fib(" + str(args.num) + ") = " + str(result))

    if args.output:
        with open("2fibonachi.txt", "a") as f:
            f.write(str(result) + '\n')

if __name__ == '__main__':
    main()