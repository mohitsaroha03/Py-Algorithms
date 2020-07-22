''

# If the str is editable
def ReversingString(str):
	s = list(str)
	end = len(str) - 1
	start = 0
	while (start < end):
		temp = s[start]
		s[start] = s[end]
		s[end] = temp
		start += 1
		end -= 1
		
	return "".join(s)

str = "CareerMonk Publications."
print ReversingString(str)

def reverse(str):
  r = ""
  for c in str:
    r = c + r
  return r
str = "CareerMonk Publications."
print reverse(str)

def ReversingString(str):
	s = list(str)
	end = len(str) - 1
	start = 0
	result = []
	while (start < end):
		s[start], s[end] = s[end], s[start]
		start += 1
		end -= 1

	return "".join(s)

str = "CareerMonk Publications."
print ReversingString(str)
