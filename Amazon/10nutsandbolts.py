class Solution:
    def matchPairs(self,nuts,bolts,n):
        def partition(arr,low,high,pivot):
            i=low
            j=low
            while(j<high):
                
                if(arr[j]<pivot):
                    arr[i],arr[j]=arr[j],arr[i]
                    i+=1
                    
                elif arr[j]==pivot:
                   arr[j],arr[high]=arr[high],arr[j]
                   j-=1
                   
                j+=1
            arr[i],arr[high]=arr[high],arr[i]
            return i       
               
        def quicksort(nuts,bolts,low,high):
            
           # pivot=arr[low]
            if low<high:
                p=partition(nuts,low,high,bolts[high])
                partition(bolts,low,high,nuts[p])
                quicksort(nuts,bolts,low,p-1)
                quicksort(nuts,bolts,p+1,high)
                
            
           
           
        quicksort(nuts,bolts,0,n-1)
                
           
       
        
        
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(nuts, bolts, n)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends