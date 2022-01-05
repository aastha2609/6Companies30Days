# https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1/

class Solution:
    def findTwoElement( self,arr, n): 
        
        ans=[0,0]
        for i in range(0,n):
                if (arr[abs(arr[i])-1])>0:
                 arr[abs(arr[i])-1]*=-1
                #  print(arr)
            # elif arr[i]<0:
                else:
                 ans[0]=abs(arr[i])
                 break
        x=ans[0]
        y=0
        for i in range (1,n+1):
            x+=i
            y+=abs(arr[i-1])
        
        ans[1]=x-y
        return ans
