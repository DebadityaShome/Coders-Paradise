'''
Implement a reverse function that receives a list as a parameter and returns the reverse of that list. 
You may create an empty list and keep adding the values in reversed order as they come from the original list.
Input #

A list
Output #

The reverse of a list
Sample Input #

[1, 2, 3, 4, 5]
Sample Output #

[5, 4, 3, 2, 1]

'''

def reverseList(input_list):
    return input_list[::-1]

print(reverseList([1, 2, 3, 4, 5]))
