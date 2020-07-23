# isGFG: , Link: 
# IsDone: 0
def canCompleteTour(self, petrol, cost):
	minVal = float("inf")
	minPos = -1
	petrolTillNow = 0
	for i in range(0, len(petrol)):
	    petrolTillNow += petrol[i] - cost[i]
	    if petrolTillNow < minVal:
		minVal = petrolTillNow
		minPos = i
	if petrolTillNow >= 0:
	    return (minPos + 1) % len(petrol)
	return -1
