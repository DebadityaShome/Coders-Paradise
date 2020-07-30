"""
Given a checkParity(n) function, write code to determine if a given number n is even or odd. Think of this as a function that returns 0 if the number is even, and 1 if it is odd. You have been given some starter code where the function and return statement have already been written, so don’t worry about any Python-specific details about functions; just implement the function logic!

Input #
A number

Output #
The parity of the number

Sample Input #
4

Sample Output #
0
"""

def checkParity(n):
    parity = n % 2
    if (parity == 0):
        return 0
    else:
        return 1

print (checkParity(23))
print (checkParity(2))
