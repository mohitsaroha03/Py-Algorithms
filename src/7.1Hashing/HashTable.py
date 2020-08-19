# Link: 
# https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/
# IsDone: 0
class HashTable:
	def __init__(self):
		self.size = 11
		self.slots = [None] * self.size
		self.data = [None] * self.size
		
	def put(self, key, data):
		hashvalue = self.hashfunction(key, len(self.slots))

		if self.slots[hashvalue] == None:
			self.slots[hashvalue] = key
			self.data[hashvalue] = data
		else:
			if self.slots[hashvalue] == key:
				self.data[hashvalue] = data  # replace
			else:
				nextslot = self.rehash(hashvalue, len(self.slots))
				while self.slots[nextslot] != None and self.slots[nextslot] != key:
					nextslot = self.rehash(nextslot, len(self.slots))

				if self.slots[nextslot] == None:
					self.slots[nextslot] = key
					self.data[nextslot] = data
				else:
					self.data[nextslot] = data  # replace

	def hashfunction(self, key, size):
	     return key % size

	def rehash(self, oldhash, size):
		return (oldhash + 1) % size	
	    
	def get(self, key):
		startslot = self.hashfunction(key, len(self.slots))

		data = None
		stop = False
		found = False
		position = startslot
		while self.slots[position] != None and  not found and not stop:
			if self.slots[position] == key:
				found = True
				data = self.data[position]
			else:
				position = self.rehash(position, len(self.slots))
				if position == startslot:
					stop = True
		return data

	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, data):
		self.put(key, data)	    
	    
H = HashTable()
H[54] = "books"
H[54] = "data"
H[26] = "algorithms"
H[93] = "made"
H[17] = "easy"
H[77] = "CareerMOonk"
H[31] = "Jobs"
H[44] = "Hunting"
H[55] = "King"
H[20] = "Lion"
print H.slots
print H.data
print H[20]

# TODO: https://practice.geeksforgeeks.org/problems/nuts-and-bolts-problem/0
# TODO: https://www.geeksforgeeks.org/sort-elements-frequency-set-4-efficient-approach-using-hash/
# TODO: https://www.geeksforgeeks.org/sort-elements-frequency-set-4-efficient-approach-using-hash/
# TODO: https://www.geeksforgeeks.org/check-if-an-array-can-be-divided-into-pairs-whose-sum-is-divisible-by-k/
# TODO: https://practice.geeksforgeeks.org/problems/a-simple-fraction/0