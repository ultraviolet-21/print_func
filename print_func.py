#Recreating the print function

def p(*params: tuple, sep: str = ' ', end: str = '') -> str:
    '''returns a string containing all arguments in order, with optional sep and end characters'''
    s = ''
    for x in range(len(params)):
        s += str(params[x])
        if x < len(params) - 1:
            s += sep
        else:
            s += end
    return s
