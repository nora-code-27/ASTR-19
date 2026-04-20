#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:31:05 2026

@author: noraballantyne
"""

class FavoriteAnimal:
    def __init__(self, armLength = 6.2, legLength = 6.2, eyeNumber = 2, tailCondition = True, furryCondition = True):
        self.armLength = armLength
        self.legLength = legLength
        self.eyeNumber = eyeNumber
        self.tailCondition = tailCondition
        self.furryCondition = furryCondition
        
    def checkTypes(self):
        typeArmLength = type(self.armLength)
        typeLegLength = type(self.legLength)
        typeEyeNumber = type(self.eyeNumber)
        typeTailCondition = type(self.tailCondition)
        typeFurryCondition = type(self.furryCondition)
        
        a = str(typeArmLength)
        b = str(typeLegLength)
        c = str(typeEyeNumber)
        d = str(typeTailCondition)
        e = str(typeFurryCondition)
                
        answer = "arm length type = " + a + "\nleg length type = " + b + "\neye number = " + c + "\ntail type = " + d+ "\nfurry type = "+ e
    
       # print("arm length type =",typeArmLength)
        #print("leg length type =",typeLegLength)
        
        return answer
        
    def describeAnimal(self):
        """
        a = str(self.armLength)
        b = str(self.legLength)
        c = str(self.eyeNumber)
        d = str(self.tailCondition)
        e = str(self.furryCondition)
        """
        
       # answer = "The animal has an arm length of = " + a + "\nThe animal has a leg length of  = " + b + "\nThe animal has this many eyes = " + c + "\nThe animal has a tail = " + d+ "\nThe animal is furry = "+ e
        #return answer
        
        print("The animal has an arm length of:",self.armLength)
        print("The animal has an leg length of:",self.legLength)
        print("The animal has this many eyes:",self.eyeNumber)
        print("The animal has a tail:",self.tailCondition)
        print("The animal is furry:",self.furryCondition)
        
   
def main():
    animalInstance = FavoriteAnimal()
   # x = animalInstance.checkTypes()
    y = animalInstance.describeAnimal()
    #print(x)
    #print( )
    #print(y)

if __name__ == "__main__":
    main()
        
        
        