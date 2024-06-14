class Solution:
    def groupAnagrams(str):
        dict = {}
        for word in str:
            sortedword = "".join(sorted(word))
            if sortedword not in dict:
                dict[sortedword] = [word]
            else:
                dict[sortedword].append(word)

        result = []
        for item in dict.values():
            result.append(item)
        return result

s=Solution
str=["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(str))
