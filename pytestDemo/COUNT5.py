def string_count(str):

    words = str.split()
    dic = {}
    for i in words:
        dic[i] = dic.get(i, 0) + 1
    return set(dic.items())

str = "sheena loves eating apple and mango her sister also loves eating apple and mango"
result=string_count(str)
print(result)