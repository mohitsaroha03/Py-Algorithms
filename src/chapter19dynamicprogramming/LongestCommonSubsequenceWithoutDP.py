# isGFG: , Link: 
# IsDone: 0
def LCSLength(X, Y):
    if not X or not Y:
        return ""
    x, m, y, n = X[0], X[1:], Y[0], Y[1:]
    if x == y:
        return x + LCSLength(m, n)
    else:
        return max(LCSLength(X, n), LCSLength(m, Y), key=len)
	
print (LCSLength('thisisatest', 'testingLCS123testing'))	
