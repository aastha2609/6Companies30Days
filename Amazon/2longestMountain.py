class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        if len(arr)<3:
            return 0
        
        maxHeight=0
        peak=False
        start=0
        i=1
        for i in range(1,len(arr)-1):
            
            if ((arr[i-1]>=arr[i] and arr[i+1]>=arr[i]) ):
                if peak==True:
                    peak=False
                    maxHeight=max(maxHeight,i-start+1)
                start=i
                
                
            elif (arr[i-1]<arr[i]>arr[i+1]):
                peak=True
                
        if peak==True:
            maxHeight=max(maxHeight,len(arr)-start)
                
                
        return maxHeight                