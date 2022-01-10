#User function Template for python3

class Solution:
    def isValid(self, mat):
        # code here
        
        # import collections
        
        rows=collections.defaultdict(set)
        column=collections.defaultdict(set)
        square=collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if mat[r][c]==0:
                    continue
                if( mat[r][c] in rows[r] or 
                   mat[r][c] in column[c] or
                   mat[r][c] in square[(r//3,c//3)]):
                       return 0
                       
                rows[r].add(mat[r][c])
                column[c].add(mat[r][c])
                square[(r//3,c//3)].add(mat[r][c])
        return 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        mat = [[0]*9 for x in range(9)]
        for i in range(81):
            mat[i//9][i%9] = int(arr[i])
        
        ob = Solution()
        print(ob.isValid(mat))
# } Driver Code Ends