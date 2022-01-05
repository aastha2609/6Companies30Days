# https://practice.geeksforgeeks.org/problems/run-length-encoding/1/

def encode(arr):
    # Code here
    s=""
    l=0
    c=arr[0]
    for i in arr:
        if c==i:
            l+=1
        else:
            s+=c+str(l)
            l=1
            c=i
    s+=c+str(l)
    return s
