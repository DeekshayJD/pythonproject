f = "frnd.txt"
f1 = "frn_d.txt"

with open(f, 'r') as fo:  # Open the file for reading
    a = fo.read()

with open(f1, 'w') as fo1:  # Open another file for writing
   # b = a.replace("friends", "batch")
    fo1.write(a)

print(a)
