# https://practice.geeksforgeeks.org/problems/count-the-subarrays-having-product-less-than-k1708/1/

def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
        i=0
        prod=1
        c=0
        x=0
        while(i<n):
            prod*=a[i]
            if a[i]>=k:
                prod=1
                x=i+1
            elif prod>=k:
                while(x<=i and prod>=k):
                    prod=prod//a[x]
                    x+=1
            c+=i-x+1
            i+=1
        return c
