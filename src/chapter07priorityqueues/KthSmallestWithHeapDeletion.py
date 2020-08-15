# Link: https://discuss.interviewbit.com/t/python-and-minheap/28532
# IsDone: 0
import heapq

def kthsmallest(A, B):
    heapq.heapify(A)
    minim = None
    for i in range(B):
        minim = heapq.heappop(A)

    return minim

print(kthsmallest([12,22,33,14,35,46,7], 2))