#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program calculates the circumference of a circle
#     with inputted radius


import random


def lowest_number_calculator(array=[]):
    lowest_number = array[0]
    counter1 = 0
    while counter1 < len(array):
        if array[counter1] < lowest_number:
            lowest_number = array[counter1]
        counter1 += 1
    return lowest_number


def main():
    # I calculate circumference

    # process
    print("Random numbers: ")
    random_numbers = []
    for counter1 in range(0, 9):
        rand_num = random.randint(1, 100)
        print(rand_num)
        random_numbers.append(rand_num)

    # call functions
    lowest_number = lowest_number_calculator(random_numbers)

    # output
    print("\nThe lowest number is {}.".format(lowest_number))
    print("\nDone.")


if __name__ == "__main__":
    main()
