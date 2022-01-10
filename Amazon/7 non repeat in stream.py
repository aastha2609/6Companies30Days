#User function Template for python3

class Solution:
    def FirstNonRepeating(self, A):
        # Code here
        
        from queue import Queue

        q=Queue()
        d={}
        output=""

        for char in A:
            if char not in d:
                q.put(char)
            d[char]=d.get(char,0)+1
            # flag=0
            while(not q.empty()):
                 if d[q.queue[0]]==1:
                     output+=q.queue[0]
                    #  flag=1
                     break
                 else:
                     q.get()
            else:
                     output+="#"
                    #  flag=1
        return output
            
                


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        A = input()
        ob = Solution()
        ans = ob.FirstNonRepeating(A)
        print(ans)

# } Driver Code Ends