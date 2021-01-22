'''
	Your task is to return the index of the pattern
	present in the given string.
	
	Function Arguments: s (given text), p(given pattern)
	Return Type: Integer.
	
'''
def strstr(s,p):
    for i in range(len(s)):
        if s[i:i+len(p)] == p:
            return i
    return -1