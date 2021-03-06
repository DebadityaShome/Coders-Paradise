"""
Given a getStr() function, write the necessary sequence of operations to 
transform the string (containing three literals) in such a way that 
every literal is tripled​ respectively.

Input: A string

Output: Triple of every string literal

Sample Input : abc

Sample Output: aaabbbccc
"""

def getStr(s):
  s=s[:1] + s[0] + s[1:]# Transform the string 
  s=s[:1] + s[0] + s[1:]
  s=s[:3] + s[3] + s[3:]
  s=s[:3] + s[3] + s[3:]
  s=s[:6] + s[6] + s[6:]
  s=s[:6] + s[6] + s[6:]
  # Update the length of string
  strlen = len(s)
  return [s, strlen]

print(getStr("abc"))
print(getStr("xyz"))

