# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 21:57:50 2025

@author: mubas
"""

########

x = 5
print(x)

########

print(type(x))
print(f"Type of the variable: {type(x)}")
print("Type of variable: "+ str(type(x)))   

#######

print(1,2,3)
print(1,2,3,sep='.')

print("Hello","World",sep=',',end='! \n')

name = "Ahin"
age = 19

print(f"Name:{name},Age:{age}",sep =',',end='.\n')


#########################

#name = input()
#name2 = input("Enter a num: ")3
#name2 = int(name2);
#print(name)
#print(name2)

#############################

a = 3
b = 4

print(b // a)
print(a ** b)

x = 5
y = 5

print(f"{x}=={y}:{x==y}")
print(f"{x}!={y} --> {x!=y}")


###############################

def fun(x):
    value = x*2
    return value


print(fun(2))