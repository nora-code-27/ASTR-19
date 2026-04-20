#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 14:28:37 2026

@author: noraballantyne
"""

def Function(x):
    y = x**3 + 8
    return y

def main():
    x = input("Input the x value: ")
    x = int(x)
    result = Function(x)
    print("The y-value for the function x^3+8 is:",result)
    if result >= 27:
        print ("YAY, the result is above 27!")

if __name__ == "__main__":
    main()