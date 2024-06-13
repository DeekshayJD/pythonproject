a = [[1,2],[1,3],[1,2],[1,3],[1,5],[5,1],[1,4]]
seen = set()
result = []

for sublist in a:
    if tuple(sublist) not in seen:
        seen.add(tuple(sublist))
        result.append(sublist)
print(seen)
print(result)