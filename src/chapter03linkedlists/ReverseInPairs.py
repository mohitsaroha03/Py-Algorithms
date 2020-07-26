#

  def reverseInPairs(self) :
    temp = self.head
    while None != temp and None != temp.get_next():
      self.swapData(temp, temp.get_next())
      temp = temp.get_next().get_next()
 
  def swapData(self, a, b):
    tmp = a.get_data()
    a.set_data(b.get_data())
    b.set_data(tmp)
