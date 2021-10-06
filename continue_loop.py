#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Oct 2021
# This program add positive numbers only


def main():
    # This program add positive numbers only
    total = 0

    # Input
    user_number = input("How many numbers are you going to add : ")

    # Process and Output
    try:
        user_number = int(user_number)
        for number_time in range(user_number):
            number_add = input("Enter a number to add : ")
            number_add = int(number_add)
            if number_add < 0:
                continue
            total = total + number_add
        print("Sum of just the positive numbers is = {0}".format(total))
    except (Exception):
        print("Invalid input")

    print("\nDone.")


if __name__ == "__main__":
    main()
