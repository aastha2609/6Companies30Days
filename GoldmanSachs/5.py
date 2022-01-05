# https://practice.geeksforgeeks.org/problems/ugly-numbers2254/1/

class Solution:
	def getNthUglyNo(self,n):
		# code here
		l=[1,2,3,4]
        if n<4:
            return l[n-1]
        a=3*2
        b=2*3
        c=1*5
    
        i=2
        j=1
        k=0
        while(len(l)<n):
            x=min(a,b,c)
            l.append(x)

            if x==a:
                i+=1
                a=2*l[i]
            if x==b:
                j+=1
                b=3*l[j]
            if x==c:
                k+=1
                c=5*l[k]
            
        return l[-1]
