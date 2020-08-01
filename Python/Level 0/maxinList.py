'''
Create a findMaximum function that receives a list as a parameter
 and returns the maximum value in the list. 
As you iterate over the list, you may want to keep track of 
the current maximum value in order to keep comparing it with the next elements of the list.

Input : A list
Output : Maximum number in the list
Sample Input : [1, 4, 9, 10, 23]
Sample Output : max = 23

​'''

def findMaximum(input_list):
    return max(input_list)

print(findMaximum([1, 4, 9, 10, 23]))