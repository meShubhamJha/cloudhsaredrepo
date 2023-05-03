# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 23:44:58 2020

@author: sumit
"""

# Python program to illustrate the concept
# of threading
# importing the threading module



def print_cube(num):
    time.sleep(5)
    print("cube: {}".format(num * num * num))


def print_square(num):
    time.sleep(5)
    print("square: {}".format(num * num))


def print_square2(num):
    time.sleep(5)
    print("square: {}".format(num * num))


def print_square3(num):
    time.sleep(5)
    print("square: {}".format(num * num))


if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(2000,))
    t2 = threading.Thread(target=print_cube, args=(2000,))
    t3 = threading.Thread(target=print_square2, args=(2000,))
    t4 = threading.Thread(target=print_square3, args=(2000,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
    t3.start()
    t4.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
    t3.join()
    t4.join()

    # both threads completely executed
    print("Done!")
