# Link: https://www.techiedelight.com/pots-gold-game-dynamic-programming/
# Function to maximize the number of coins collected by a player,
# assuming that opponent also plays optimally
def optimalStrategy(coin, i, j, lookup):
 
    # base case: one pot left, only one choice possible
    if i == j:
        return coin[i]
 
    # if we're left with only two pots, choose one with maximum coins
    if i + 1 == j:
        return max(coin[i], coin[j])
 
    # if sub-problem is seen for the first time, solve it and
    # store its result in a lookup table
    if lookup[i][j] == 0:
        # if player chooses front coin i, opponent is left to choose
        # from [i+1, j].
        # 1. if opponent chooses front coin i+1, recur for [i+2, j]
        # 2. if opponent chooses rear coin j, recur for [i+1, j-1]
 
        start = coin[i] + min(optimalStrategy(coin, i + 2, j, lookup),
                              optimalStrategy(coin, i + 1, j - 1, lookup))
 
        # if player chooses rear coin j, opponent is left to choose
        # from [i, j-1].
        # 1. if opponent chooses front coin i, recur for [i+1, j-1]
        # 2. if opponent chooses rear coin j-1, recur for [i, j-2]
 
        end = coin[j] + min(optimalStrategy(coin, i + 1, j - 1, lookup),
                            optimalStrategy(coin, i, j - 2, lookup))
 
        # assign maximum of two choices
        lookup[i][j] = max(start, end)
 
    # return the subproblem solution from the dict
    return lookup[i][j]
 
 
if __name__ == '__main__':
 
    # pots of gold arranged in a line
    coin = [4, 6, 2, 3]
 
    # Create a table to store solutions of subproblems
    lookup = [[0 for x in range(len(coin))] for y in range(len(coin))]
 
    print("Maximum coins collected by player is",
          optimalStrategy(coin, 0, len(coin) - 1, lookup))