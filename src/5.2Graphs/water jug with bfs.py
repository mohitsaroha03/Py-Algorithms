# Link: https://leetcode.com/problems/water-and-jug-problem/discuss/318231/Python-solution-using-BFS
def canMeasureWater(self, x: int, y: int, z: int) -> bool:
    
    if (x + y < z):
        return False
    
    queue = [0]
    
    visited = {}
    
    total = x + y
    
    while len(queue) != 0:
        
        current = queue.pop()
        
        if current + x <= total and current + x not in visited:
            
            queue.append(current+x)
            
            visited[current+x] = True
        
        if current - x >= 0 and current - x not in visited:
            
            queue.append(current - x)
            
            visited[current-x] = True
        
        if current + y <= total and current + y not in visited:
            
            queue.append(current + y)
            
            visited[current + y] = True
        
        if current - y >= 0 and current - y not in visited:
            
            queue.append(current - y)
            
            visited[current - y] = True
        
        if current == z:
            return True
    
    return False