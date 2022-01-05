# https://practice.geeksforgeeks.org/problems/decode-the-string2444/1

def decodedString(s):
    n=len(s)
    def process(ind):
        nonlocal s
        ans=''
        while ind<n and s[ind]!=']':
            c=s[ind]
            if ord(c)<97:
                j=ind
                while s[j]!='[':
                    j+=1
                c = s[ind:j]
                ss,ind = process(j+1)
                ans+= ss*int(c)
            else:
                ans+=c
            ind+=1
        return ans,ind
    return process(0)[0]
