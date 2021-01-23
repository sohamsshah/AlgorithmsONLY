#User function Template for python3

'''
	Your task is tocheck if the given two strings
	are rotations of each other.
	Function Arguments: s1 and s2 (given strings)
	Return Type:boolean
'''

def areRotations(s1,s2):
    if len(s1) != len(s2):
        return False
    rotator = 0
    s1, s2 = list(s1), list(s2)
    while rotator != len(s2):
        val = s2.pop(0)
        s2.append(val)
        if s2 == s1:
            return True
        rotator+=1
    return False