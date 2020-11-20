# Link - https://leetcode.com/problems/verifying-an-alien-dictionary/
# Link2 - https://www.geeksforgeeks.org/given-sorted-dictionary-find-precedence-characters/

def isAlienSorted(self, words: list[str], order: str) -> bool:
    d = {c: i for i, c in enumerate(order)}

    for i in range(len(words) - 1):
        w1 = words[i]
        w2 = words[i + 1]
        for j in range(min(len(w1), len(w2))):
            if d[w1[j]] < d[w2[j]]:
                break
            elif w1[j] == w2[j]:
                continue
            else:
                return False
        else:
            if len(w1) > len(w2): return False
    return True


#Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
#Output: true
#Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
