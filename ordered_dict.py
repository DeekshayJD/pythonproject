from collections import OrderedDict

# OrderedDict explicitly maintains insertion order
ordered_dict = OrderedDict()
ordered_dict['apple'] = 1
ordered_dict['banana'] = 2
ordered_dict['cherry'] = 3

print("\nOrderedDict:")
for key, value in ordered_dict.items():
    print(f"{key}: {value}")

# Output will be in the order of insertion
# apple: 1
# banana: 2
# cherry
