"""
Given a string, use a findOccurence(s) function that allows you 
to find the first occurrences of "b" and "ccc"​ in the string.

Input: A string
Output: The first occurrence of “b” and “ccc” in the string

Sample Input #
aaabbbccc
Sample Output #
[3, 6]
"""
def findOccurence(s):
    a = s.find("b")
    b = s.find("ccc")
    return [a, b]
print (findOccurence("aaabbbccc"))

