
def hasLeadingZeroes(string):
    if string != str(int(string)):
        return False
    return True
def isValid(s):
    #code here
    s = list(s.split('.'))
    if len(s) != 4:
        return False
    for i in s:
        if i.isdigit() == False:
            return False
        if int(i) not in range(0,256):
            return False
        if hasLeadingZeroes(i) == False:
            return False
    return True