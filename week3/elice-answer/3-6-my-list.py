import random


def my_list(num):
    mylist = []
    for i in range(num):
        mylist.append(random.randint(0, 100))
    return mylist


print(my_list(10))
