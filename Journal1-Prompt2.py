#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 14:00:23 2026

@author: noraballantyne
"""

def Additon(num1,num2):
    sum = num1 + num2
    print(sum)
    print(type(sum))
    
def Division(num1,num2):
    division = num1/num2
    division = int(division)
    remainder = num1%num2
    print("The solution is:",division)
    print("The remainder is:",remainder)
    print(type(division))
    
def Multiplication(num1,num2):
    product = num1*num2
    print("The product is:",product)
    print(type(product))
    
def main():
    i = input("Press 1 for Addition, 2 for Division, 3 for Multipication: ")
    i = int(i)
    if i ==1:
        numInput1 = input("Please write the first float you want to add: ")
        numImput1 = float(numInput1)
        numInput2 = input("Please write the second float you want to add: ")
        numImput2 = float(numInput2)
        Additon(numImput1,numImput2)
    if i==2:
        numInput1 = input("Please input the numerator: ")
        numImput1 = int(numInput1)
        numInput2 = input("Please input the denominator: ")
        numImput2 = int(numInput2)
        Division(numImput1,numImput2)
    if i==3:
        numInput1 = input("Please input the float: ")
        numImput1 = float(numInput1)
        numInput2 = input("Please input the integer: ")
        numImput2 = int(numInput2)
        Multiplication(numImput1,numImput2)
    
if __name__ == "__main__":
    main()