''

import random
def shuffle(cards):
    max = len(cards) - 1
    while max != 0:
        r = random.randint(0, max)
        cards[r], cards[max] = cards[max], cards[r]
        max = max - 1
    return cards

actual = range(1, 53)
shuffle(actual)
