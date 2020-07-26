#

def nthNodeFromEnd(self, n):
    if 0 > n:
      return None
 
    # count k units from the self.head.
    temp = self.head
    count = 0
    while count < n and None != temp:
      temp = temp.next
      count += 1
 
    # if the LinkedList does not contain k elements, return None
    if count < n or None == temp:
      return None
 
    # keeping tab on the nth element from temp, slide temp until
    # temp equals self.tail. Then return the nth element.
    nth = self.head
    while None != temp.next:
      temp = temp.next
      nth = nth.next
 
    return nth
