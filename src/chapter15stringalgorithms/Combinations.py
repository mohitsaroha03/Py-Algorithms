# isGFG: , Link: 
# IsDone: 0
def combinationByRecursion(elems, s, idx, li):
    for i in range(idx, len(elems)):
        s += elems[i]
        li.append(s)
        # print s, idx
        combinationByRecursion(elems, s, i + 1, li)
        s = s[0:-1]

def combinationByIteration(elems):
    level = ['']
    for i in range(len(elems)):
        nList = []
        for item in level:
            nList.append(item + elems[i])
        level += nList
    return level[1:]

res = []
combinationByRecursion('abc', '', 0, res)
print combinationByIteration('abc')
print combinationByIteration('abc')
