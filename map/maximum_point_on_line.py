from collections import defaultdict
import numpy as np
def maxPoints(points):
        if len(points)<=2:
            return len(points)
        def solve(p1,p2):
            x1,y1=p1
            x2,y2=p2
            if x1==x2:
                #vertical
                return float('inf'),x1
            #here we using long double for more accurate result
            slope=(y2-y1)*np.longdouble(1)/(x2-x1)
            intercept=y2-slope*x2
            return slope,intercept
        res=0
        dic=defaultdict(set)
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                slope,intercept=solve(points[i],points[j])
                dic[(slope,intercept)].add(i)
                dic[(slope,intercept)].add(j)
                res=max(res,len(dic[(slope,intercept)]))
        return res
arr=[[1,1],[2,2],[3,3]]
print(maxPoints(arr))