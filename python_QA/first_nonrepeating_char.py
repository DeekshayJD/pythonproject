#given string find the first non repeating character index,ie 1 if not exist return -1
#i/p="leetcode
#o/p=1

def non_repeating_index(s):
    count_char={}
    for char in s:
        count_char[char]=count_char.get(char,0)+1

    for i,char  in enumerate(s):
        if count_char[char]==1:
            return i
    return -1




str="eedcd"
print(non_repeating_index(str))