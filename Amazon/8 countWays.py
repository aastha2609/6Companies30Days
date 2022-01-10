#User function Template for python3

class Solution:
    
    #Function to count number of ways to reach the nth stair 
    #when order does not matter.
    def countWays(self,m):
        
        mod = 1000000007
        if m==1 or m==2:
            return m
        # code here
        dp=[0 for i in range(m+1)]
        dp[0]=0
        dp[1]=1
        dp[2]=2
        
        
            
        for i in range(3,m+1):
            # count=0
            dp[i]+=1+dp[i-2]########################Doubt
            dp[i]=dp[i]%mod
            
        return dp[-1]
            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))

# } Driver Code Ends