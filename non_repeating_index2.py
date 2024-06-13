def non_repeating_index(s):
    char_count={}
    for char in s:
        char_count[char]=char_count.get(char,0)+1

    for i,char in enumerate(s):
       if char_count[char]==1:
           return i
    return -1
s="eedced"
print(non_repeating_index(s))