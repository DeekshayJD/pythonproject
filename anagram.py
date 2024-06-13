def is_anagram(s, t):
    # Check if the sorted versions of the strings are equal
    return sorted(s)==sorted(t)


    #print(t)

# Test cases
s1 = "anagram"
t1 = "nagaram"
print(is_anagram(s1, t1))  # Output: True

'''
s2 = "rat"
t2 = "cat"
print(is_anagram(s2, t2))  # Output: False
'''
