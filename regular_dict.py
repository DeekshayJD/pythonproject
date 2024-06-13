# Regular dictionary (insertion order maintained since Python 3.7)
normal_dict = {}
normal_dict['apple'] = 1
normal_dict['banana'] = 2
normal_dict['cherry'] = 3

print("Regular Dictionary:")
for key, value in normal_dict.items():
    print(f"{key}: {value}")

# Output will be in the order of insertion
# apple: 1
# banana: 2
# cherry: 3
