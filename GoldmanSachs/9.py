# https://practice.geeksforgeeks.org/problems/number-following-a-pattern3126/1

def printMinNumberForPattern(S):
    ind=0
    n=len(S)
    num='1'
    ans=''
    while ind<n:
        if S[ind]=='D':
            num=str(ind+2)+num
        else:
            ans+=num
            num=str(ind+2)
        ind+=1
    ans+=num
    return ans
