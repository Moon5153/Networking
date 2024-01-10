# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 10:09:57 2022

@author: Najmun
ID: 301160081
"""


import matplotlib.pyplot as plt
import math
import random

number_of_values = 250


class Generator:
    
    def __init__(self, minValue = 18, maxValue = 21, start_offset=0,increment=0.1) -> None:
        self.min = minValue
        self.max = maxValue
        self.start_offset = start_offset
        self.increment = increment

    def generator_1(self) -> int:
    
        #This generator gives a random number in a 15 to 21
        return self.sine() + random.randint(-10, 10)/50

    def sine(self):
        self.start_offset += self.increment
        return math.sin(self.start_offset)
        
    @property
    def value (self):
        m=self.max - self.min
        x=self.generator_1()
        c=self.min
        y = (m*x)+c
        return y
    

#gen = Generator()
#res=[gen.value for x in range(number_of_values)]


#if __name__ == '__main__':
    #plt.title("Indoor Temperature at Progress Campus")
    #plt.xlabel("Time")
   # plt.ylabel("Temperature (degree C)")
    #plt.plot(res)
    #plt.show()
    
  

    