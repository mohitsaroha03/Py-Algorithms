# isGFG: , Link: 
# IsDone: 0
# @param s, a string
# @return a string
def reverseWordsInSentence(self, s):
	result = []
	inWord = False
	for i in range(0, len(s)):
	    if (s[i] == ' ' or s[i] == '\t') and inWord:
		inWord = False
		result.insert(0, s[start:i])
		result.insert(0, ' ')
	    elif not (s[i] == ' ' or s[i] == '\t' or inWord):
		inWord = True
		start = i
	if inWord:
	    result.insert(0, s[start:len(s)])
	    result.insert(0, ' ')
	if len(result) > 0:
	    result.pop(0)
	return ''.join(result)
