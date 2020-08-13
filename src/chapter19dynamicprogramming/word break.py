# Link: https://www.techiedelight.com/word-break-problem/

# Function to determine if can be segmented into a space-separated
# sequence of one or more dictionary words
def wordBreak(dict, str):

	# return true if we have reached the end of the String,
	if not str:
		return True

	for i in range(1, len(str) + 1):

		# consider all prefixes of current String
		prefix = str[:i]

		# return true if prefix is present in the dictionary and remaining
		# also forms space-separated sequence of one or more
		# dictionary words
		if prefix in dict and wordBreak(dict, str[i:]):
			return True

	# return false if the can't be segmented
	return False


if __name__ == '__main__':

	# List of Strings to represent dictionary
	dict = ["self", "th", "is", "famous", "Word",
			"break", "b", "r", "e", "a", "k", "br",
			"bre", "brea", "ak", "problem"]

	# input String
	str = "Wordbreakproblem"

	if wordBreak(dict, str):
		print("String can be segmented")
	else:
		print("String can't be segmented")
