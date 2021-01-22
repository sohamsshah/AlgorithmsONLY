# Return true if str is binary, else false
def isBinary(str):
    string = set(str)
    if string == {'0','1'} or string == {'0'} or string == {'1'}:
        return True
    return False