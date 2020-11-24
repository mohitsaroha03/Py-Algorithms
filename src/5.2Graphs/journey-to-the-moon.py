# Link - https://www.hackerrank.com/challenges/journey-to-the-moon/
# Solution - https://www.hackerrank.com/rest/contests/master/challenges/journey-to-the-moon/hackers/jven/download_solution?primary=true
# https://www.youtube.com/watch?v=IeZs94EFCTk

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.rank = 0
        self.descendents = 1

    def union(self, other):
        r1 = self.find()
        r2 = other.find()
        if r1 == r2:
            return
        if r1.rank < r2.rank:
            r1.parent = r2
            r2.descendents += r1.descendents
        elif r1.rank > r2.rank:
            r2.parent = r1
            r1.descendents += r2.descendents
        else:
            r2.parent = r1
            r1.descendents += r2.descendents
            r1.rank += 1

    def find(self):
        return self if self.parent is None else self.parent.find()


def get_ans(astros, pairs):
    nodes = [Node(astro) for astro in range(astros)]
    for pair in pairs:
        nodes[pair[0]].union(nodes[pair[1]])
    sizes = [root.descendents for root in nodes if root.find() == root]
    sq = lambda x: x * x
    return (sq(sum(sizes)) - sum(map(sq, sizes))) / 2


if __name__ == '__main__':
    astros, lines = map(int, raw_input().split())
    pairs = []
    for i in range(lines):
        pair = tuple(map(int, raw_input().split()))
        pairs.append(pair)
    print(get_ans(astros, pairs))
