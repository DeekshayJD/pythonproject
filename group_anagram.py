def group_anagram(str):
    dic={}
    for word in str:
        sorted_word="".join(sorted(word))
        if sorted_word not in dic:
            dic[sorted_word]=[word]
        else:
            dic[sorted_word].append(word)


    result=[]
    for item in dic.values():
     result.append(item)

    return result

str=["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagram(str))