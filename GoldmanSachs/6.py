# https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s=""
        a=min(len(str1),len(str2))
        for i in range(a):
            if str1[i]==str2[i]:
                s+=str1[i]
            else:
                break
        x=""
        # print(s)
        if s=="":
            return s
        if len(s)!=a:
            return ""
        else:
            b=""
            if len(str1)>=len(str2):
                for i in s:
                    b+=i
                    if len(str1)%len(b)==0:
                        if str1==(len(str1)//len(b))*b:
                            break
            else:
                for i in s:
                    b+=i
                    if len(str2)%len(b)==0:
                        if str2==(len(str2)//len(b))*b:
                            break
            # print(b)
            if b*(len(str1)//len(b))==str1 and b*(len(str2)//len(b))==str2:
                i=a
                r=a//len(b)
                while(r>0):
                    if len(str1)%i==0 and len(str2)%i==0:
                    # print(i)
                        return b*r
                    r-=1
                    i=r*len(b)
            else:
                return ""
