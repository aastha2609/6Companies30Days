#https://practice.geeksforgeeks.org/problems/print-anagrams-together/1/&sa=D&source=editors&ust=1641374913343000&usg=AOvVaw0Kcsf6STU2uDBI5AFCJUYO

d={}
        for i in words:
            a=sorted(i)
            a="".join(a)
            # print(a)
            if a in d:
                d[a].append(i)
            else:
                d[a]=[i]
        # print(d)
        l=[]
        for i in d:
            l.append(d[i])
        return l
