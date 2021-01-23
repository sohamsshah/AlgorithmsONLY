from collections import OrderedDict 
'''
	Your task is to check if the given strings are
	isomorphic or not.
	
	Function Arguments: str1 and str2 (given strings)
	Return Type: boolean

'''
def areIsomorphic(str1,str2):
    dict1 = OrderedDict()
    dict2 = OrderedDict()
    
    for i in str1:
        if i not in dict1:
            dict1[i] = 0
        dict1[i]+=1
    
    for i in str2:
        if i not in dict2:
            dict2[i] = 0
        dict2[i]+=1
    return (list(dict1.values())== list(dict2.values()))