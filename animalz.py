def read_file():
    with open('animal-dataset.txt') as f:
        mylist = [tuple(i.split(',')) for i in f.read().splitlines()]
        print(mylist)


read_file()
