#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:44:38 2026

@author: noraballantyne
"""
import numpy as np
from astropy.table import Table
from astropy.io import ascii 
from astropy.io import fits 

def preTable():
    pi = np.pi
    pi = pi * 2
    x = np.linspace(0,pi,1000)
    sinX = np.sin(x)
    
    table = Table([x,sinX],names = ["x","sin(x)"])
    ascii.write(table, 'table.txt', format='commented_header') 
    table_in = ascii.read('table.txt')
    print(table_in)
    
def X():
    pi = np.pi
    pi = pi * 2
    xArray = np.linspace(0,pi,1000)
    for i in range(1000):
        x = xArray[i]
        sinX = np.sin(x)
        if sinX == np.sin(2*np.pi):
            sinX = 0
    
        print(f"{x:6.5f}" + " | " + f"{sinX:6.5f}")
        

    
def main():
    print("   x    |  sin(x)")
    print("-----------------")
    X()

if __name__ == "__main__":
    main()
