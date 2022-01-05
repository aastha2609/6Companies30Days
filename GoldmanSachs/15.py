# https://practice.geeksforgeeks.org/problems/array-pair-sum-divisibility-problem3257/1

class Solution:
	def canPair(self, nuns, k):
		# Code here
		d={}
		for i in nums:
		    d[i%k]=d.get(i%k,0)+1
		for i in d:
		    if i==0 and d[i]%2!=0:
		        return False
		    if i==0 and d[i]%2==0:
		        continue
		    elif k-i not in d:
		        return False
		    elif i==k-i and d[k-i]%2!=0:
		        return False
		    elif d[i]!=d[k-i]:
		        return False
		return True
