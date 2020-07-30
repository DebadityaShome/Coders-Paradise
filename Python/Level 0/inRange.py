"""
Given an inRange(x,y) function, 
write a method that determines whether a given pair (x, y) falls in the range (x < 1/3 < y). 
Essentially, you’ll be implementing the body of a function that
takes in two numbers x and y and returns True if x < 1/3 < y; otherwise, it returns False.
"""

def inRange(x,y):
    return (x < 1/3 < y)

x = float(input("First number ? ").strip())
y = float(input("Second number ? ").strip())
print(inRange(x,y))