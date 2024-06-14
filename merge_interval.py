def merge_interval(interval):
    interval.sort(key=lambda x:x[0])
    i=1
    while i<len(interval):
        if interval[i][0]<=interval[i-1][1]:
            interval[i-1][0]=min(interval[i-1][0],interval[i][0])
            interval[i-1][1]=max(interval[i-1][1],interval[i][1])
            interval.pop(i)
        else:
            i=i+1
    return interval






interval=[[1,3],[2,6],[8,12],[14,18]]
print(merge_interval(interval))