# Link: 
# IsDone: 0
myString = "We want to get the counts for each letter in this sentence"
counts = {}

for letter in myString:
    counts[letter] = counts.get(letter, 0) + 1
print counts

sortedKeys = sorted(counts.keys(), key=lambda x: counts[x])
for k in sortedKeys:
    print k , "-->" , counts[k]
