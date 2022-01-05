# https://practice.geeksforgeeks.org/problems/overlapping-rectangles1924/1/

def doOverlap(self, l1, r1, l2, r2):
    if (min(l1[1],l2[1])-max(r2[1],r1[1]))<0:
        return 0
        
    if (min(r1[0],r2[0])-max(l1[0],l2[0]))<0:
        return 0
        
    return 1
