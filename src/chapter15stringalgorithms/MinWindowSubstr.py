# isGFG: , Link: 
# IsDone: 0
def minWindowSubstr(inputStr, pattern):
    if inputStr == '' or pattern == '': return ''
    last_seen = {}
    start = 0; end = len(inputStr) - 1
    pattern = set(pattern)
    # find such a substring ended at i-th character.
    for i, ch in enumerate(inputStr):
        if ch not in pattern: continue
        last_seen[ch] = i
        if len(last_seen) == len(pattern):
            # all chars have been seen
            first = min(last_seen.values())  # **We can use a priority queue, O(logn)
            if i - first + 1 < end - start + 1:
                start = first; end = i
    
    window = inputStr[start:end + 1] if len(last_seen) == len(pattern) else ""
    # print window, len(window)
    return window


print minWindowSubstr("XFDOYEZODEYXNZD", "XYZF")
print minWindowSubstr("XXXYDFYFFHGKOXXFDOPPQDQPFVZZDEZ", "XZD")
print minWindowSubstr("XXXYYYY", "XY")
print minWindowSubstr("", "")
