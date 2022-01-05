# https://practice.geeksforgeeks.org/problems/total-decoding-messages1235/1/

def CountWays(s):
	n=len(s)
	if s[0]=='0':return 0
	ans = [0]*(n+1)
	ans[0]=ans[1]=1
	for i in range(2,n+1):
	    j=i-1
	    if s[i-2]!='0' and int(s[i-2:i])<=26:
	        ans[i]=ans[i-2]
	    if s[i-1]!='0':
	        ans[i]+=ans[i-1]
	print(ans)
	return ans[-1]%(1000000007)
