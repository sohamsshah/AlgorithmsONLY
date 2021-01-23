#User function Template for python3
from collections import Counter
'''Your task is to check given two strings
   are anagrams or not.
   a,b: given strings
   
   Return True or False accordingly.
   
   -> You don't need to print anything.Return type of function
   is boolean.
'''

def isAnagram(a,b):
    return Counter(a) == Counter(b)