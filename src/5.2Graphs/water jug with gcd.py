# Link: https://leetcode.com/problems/water-and-jug-problem/discuss/426730/Very-Simple-Python-Solution
# IsDone: 0
def canMeasureWater(self, x, y, z):
    if z == 0:
        return True
    if x+y<z:
        return  False
    return z % self.gcd(x, y) == 0;
    
def gcd(self,a,b):
    if a%b == 0:
        return b
    else :
        return self.gcd(b,a%b)
