def example_1():
    with open(r'./sample.txt') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            print('end of the file')


def example_2():
    with open(r'./sample.txt') as f:
        while True:
            line = next(f)
            print(line, end='')


if __name__ == '__main__':
    example_2()
