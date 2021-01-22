#User function Template for python3

"""
input - 
@s = given string 

output - 
return -1 or required ans
"""
def missingPanagram(s):
    ideal_panagram = 'abcdefghijklmnopqrstuvwxyz'
    ideal_panagram = list(ideal_panagram)
    ans = ""
    s = s.lower()
    for i in range(len(s)):
        if s[i] >= 'a' and s[i] <= 'z':
            ideal_panagram[ord(s[i]) - ord('a')] = '#'
    for i in ideal_panagram:
        if i != '#':
            ans+=i
    return ans