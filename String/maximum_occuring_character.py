#User function Template for python3


'''
	Your task is to return the lexicographically smallest 
	max occuring charcter in given string.
	
	Function Arguments: s (given string)
	Return Type: char or -1.
	
'''

def getMaxOccurringChar(s):
    hashmap = {}
    for i in s:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i]+=1
    
    ans=''
    maxi=0
    for i in hashmap:
        if hashmap[i] > maxi:
            maxi = hashmap[i]
            ans = i
        elif hashmap[i] == maxi:
            if ans > i:
                ans = i
    return ans