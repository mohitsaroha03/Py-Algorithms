#

class AddingListNumbers:
    def addTwoNumbers(self, list1, list2):
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        len1 = 0
        len2 = 0
        
        head = list1
        while head != None:
            len1 += 1
            head = head.next
        
        head = list2
        while head != None:
            len2 += 1
            head = head.next
        
        if len1 >= len2:
            longer = list1
            shorter = list2
        else:
            longer = list2;
            shorter = list1
        
        sum = None
        
        carry = 0
        
        while shorter != None:
            value = longer.data + shorter.data + carry
            carry = value / 10
            value -= carry * 10
            
            if sum == None:
                sum = Node(value)
                result = sum
            else:
                sum.next = Node(value)
                sum = sum.next
                
            longer = longer.next
            shorter = shorter.next
            
        while longer != None:
            value = longer.data + carry
            carry = value / 10
            value -= carry * 10
            
            sum.next = Node(value)
            sum = sum.next
            
            longer = longer.next
            
        if carry != 0:
            sum.next = Node(carry)
        
        return result
