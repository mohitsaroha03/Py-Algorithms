# Link: https://leetcode.com/problems/word-ladder/discuss/905779/python-solution.-Simple.-Readable-code
# IsDone: 0
def bucket(newList):
    	hold = {}
	for word in newList:
		for i in xrange(len(word)):
			key = word[:i]+"_"+word[i+1:]
			if key not in hold:
				hold[key] = []
			hold[key].append(word)
	return hold

def buildGraph(container):
	graph = {}
	for key in container:
		for word1 in container[key]:
			for word2 in container[key]:
				if word1 != word2:
					if word1 not in graph:
						graph[word1]=set()
					graph[word1].add(word2)
	return graph

def bfs(beginWord,endWord, wordList):
	container = bucket([beginWord]+wordList)
	graph = buildGraph(container)
	seen = set([beginWord])
	pq = deque([(beginWord,1)])
	while pq:
		node,depth = pq.popleft()
		if node == endWord:
			return depth
		if node in graph:
			for nexxt in graph[node]:
				if nexxt not in seen:
					seen.add(nexxt)
					pq.append((nexxt,depth+1))
	return 0

if endWord not in wordList: return 0
return bfs(beginWord, endWord,wordList)