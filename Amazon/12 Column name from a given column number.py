#User function Template for python3

class Solution:
    def colName (self, n):
        # your code here
        # def titleToNumber(self, s):   
        s=""
        while(n>0):
            ch=(ord('A')+(n-1)%26)
            # print(chr(ch))
            s+=chr(ch)
            n=(n-1)//26
            
        return s[::-1]
            
    
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    ob = Solution()
    print (ob.colName (n))
    

# } Driver Code Ends