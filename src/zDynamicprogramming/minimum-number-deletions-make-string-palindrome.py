# Link: https://www.geeksforgeeks.org/minimum-number-deletions-make-string-palindrome/
# function defenation
def transformation(s1,s2,i,j,dp): 
	
	# base cases
	if i>=len(s1) or j>=len(s2):
		return 0
	
	# checking the ndesired condition
	if s1[i]==s2[j]: 
		
		# if yes increment the cunt
		dp[i][j]=1+transformation(s1,s2,i+1,j+1,dp) 
		
	# if no 
	if dp[i][j]!=-1: 
		
		#return the value form the table
		return dp[i][j] 
	
	# else store the max tranforamtion
	# from the subsequence
	else: 
		dp[i][j]=max(transformation(s1,s2,i,j+i,dp),
					transformation(s1,s2,i+1,j,dp))
		
	# return the dp [-1][-1] 
	return dp[-1][-1] 

					

s1 = "geeksforgeeks"
s2 = "geeks"
i=0
j=0

#initialize the array with -1
dp=[[-1 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)] 
print("MINIMUM NUMBER OF DELETIONS: ",
	len(s1)-transformation(s1,s2,0,0,dp),
	end=" ")
print("MINIMUM NUMBER OF INSERTIONS: ",
	len(s2)-transformation(s1,s2,0,0,dp),
	end=" " )
print("LCS LENGTH: ",transformation(s1,s2,0,0,dp))