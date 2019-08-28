def f_range(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


if __name__ == '__main__':
    for n in f_range(0, 6, 0.73):
        print(n)

    print(f_range(0, 6, 0.73))
    print(list(f_range(0, 6, 0.73)))

    gen = f_range(0, 6, 0.73)

    print()
    print('printing geg...')
    for g in gen:
        print(g)
