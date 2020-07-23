# isGFG: , Link: 
# IsDone: 0
def wildcardMatch(inputString, pattern):
    if len(pattern) == 0: 
	    return len(inputString) == 0
    # inputString can be empty
    if pattern[0] == '?':
        return len(inputString) > 0 and wildcardMatch(inputString[1:], pattern[1:])
    elif pattern[0] == '*':
        # match nothing or
        # match one and continue, AB* = A*
        return wildcardMatch(inputString, pattern[1:]) or \
               (len(inputString) > 0 and wildcardMatch(inputString[1:], pattern))
    else: 
        return len(inputString) > 0 and inputString[0] == pattern[0] and wildcardMatch(inputString[1:], pattern[1:])
    
    return 0

print wildcardMatch("cc", "c")
print wildcardMatch("cc", "cc")
print wildcardMatch("ccc", "cc")
print wildcardMatch("cc", "*")
print wildcardMatch("cc", "a*")
print wildcardMatch("ab", "?*")
print wildcardMatch("cca", "c*a*b")
