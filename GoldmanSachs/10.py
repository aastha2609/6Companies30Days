import heapq as hp, random
def max10(arr,num=10):
    h=[]
    for i in arr:
        if len(h)==0:
            h.append(i)
        if i>h[0]:
            hp.heappush(h,i)
            if len(h)>num:
                hp.heappop(h)
    return h
    

if __name__=='__main__':
    arr = list(range(1000000000))
    random.shuffle(arr)
    print(max10(arr))
