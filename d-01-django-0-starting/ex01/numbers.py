def my_numbers():
    with open("numbers.txt", "r") as filein:
        numbers = list(map(int, filein.read().strip().split(',')))
        filein.close()
    for n in numbers:
        print(n)


if __name__ == '__main__':
    my_numbers()
