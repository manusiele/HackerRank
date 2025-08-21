#!/bin/python3

import math
import os
import random
import re
import sys


class VendingMachine:
    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price

    def buy(self, req_items, money):
        if req_items > self.num_items:
            raise ValueError("Not enough items in the machine")
        if money < req_items * self.item_price:
            raise ValueError("Not enough coins")
        
        self.num_items -= req_items
        change = money - (req_items * self.item_price)
        return change


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")

    fptr.close()


#     The question involves implementing a VendingMachine class in Python based on specific requirements for a vending machine simulation. Here's a description of the problem:

# Objective: Create a VendingMachine class that manages a stock of items and handles purchase requests according to given rules.
# Initialization: The class is instantiated using a constructor VendingMachine(num_items, item_price), where:

# num_items is the initial number of items in the machine.
# item_price is the number of coins required to buy a single item.


# Method: The class must implement a buy(req_items, money) method, which represents a buy request where:

# req_items is the number of items the customer wants to purchase.
# money is the amount of money (in coins) the customer inserts.


# Behavior:

# If there are enough items in the machine to fulfill the request and the inserted money is sufficient (i.e., money >= req_items * item_price), the method:

# Reduces the number of items in the machine by req_items.
# Returns the change as an integer (i.e., money - (req_items * item_price)).


# If there are fewer items in the machine than requested (req_items > num_items), it raises a ValueError with the message "Not enough items in the machine".
# If there are enough items but the money is insufficient (money < req_items * item_price), it raises a ValueError with the message "Not enough coins".


# Input Format: The program reads input from standard input (stdin) as follows:

# The first line contains two space-separated integers: num_items and item_price to initialize the vending machine.
# The second line contains an integer n, the number of operations to perform.
# The next n lines each contain two space-separated integers: req_items and money for each buy request.


# Output: The program writes the result of each operation to a file:

# The change (an integer) if the purchase is successful.
# The error message as a string if a ValueError is raised.


# Constraints: There will be at most 100 operations to be performed.
# Testing: The implementation is tested with a provided code stub and input files, where each input file contains parameters to test the implementation. The results of the operations are printed to standard output.
