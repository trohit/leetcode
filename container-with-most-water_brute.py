class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0  
        minleftpos = 0
        n = len(height)
        for i in range(n):
            th = height[i]
            # find min left pos
            j = i-1
            while j>=0:
                l = min(height[i],height[j])
                b = i-j          
                #print(f"i:{i}->{j} 2 x min({height[i]},{height[j]}) x {i- j} max: {maxarea}")
                tarea = l * b
                narea = max(maxarea, tarea)
                if narea != maxarea:
                    # print(f"{l}x{b} = {tarea} max {maxarea}, {tarea}")
                    maxarea = narea                
                j-=1
            i+=1
        return maxarea
        
