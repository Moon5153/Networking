# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 10:43:08 2022

@author: Najmun Nahar
ID: 301160081
Mid Term Test
"""

class Person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

class Customer(Person):
    def __init__(self, name, address, phone, customNum, mailCheck):
        Person.__init__(self, name, address, phone)
        self.customNum = customNum
        self.mailCheck = mailCheck

customer = Customer("Najmun Nahar", "12 Teesdale Place, Scarborough", 6471561234, 101, True)

print("Name: " + customer.name + "\nAddress: " +customer.address+ "\nTelephone: "+str(customer.phone)+"\nCustomer Number: "+str(customer.customNum)+"\nWish to be on Mail List: "+str(customer.mailCheck))
