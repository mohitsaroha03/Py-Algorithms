# Link: https://www.geeksforgeeks.org/find-the-maximum-amount-that-can-be-collected-by-selling-movie-tickets/
# Python 3 implementation of the approach 
# TODO: pending
# Function to return the maximum amount 
# that can be collected by selling tickets 
def maxAmount(M, N, seats): 
	
	# Priority queue that stores 
	# the count of empty seats 
	q = [] 

	# Insert each array element 
	# into the priority queue 
	for i in range(M): 
		q.append(seats[i]) 

	# To store the total 
	# number of tickets sold 
	ticketSold = 0

	# To store the total amount 
	# of collection 
	ans = 0

	# While tickets sold are less than N 
	# and q.top > 0 then update the collected 
	# amount with the top of the priority 
	# queue 
	q.sort(reverse = True) 
	while (ticketSold < N and q[0] > 0): 
		ans = ans + q[0] 
		temp = q[0] 
		q = q[1:] 
		q.append(temp - 1) 
		q.sort(reverse = True) 
		ticketSold += 1

	return ans 

# Driver code 
if __name__ == '__main__': 
	seats = [1, 2, 4] 
	M = len(seats) 
	N = 3

	print(maxAmount(N, M, seats)) 