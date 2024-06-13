n=[[10,20,30],[40,50,60],[70,80,90]]
print("element in row wise:-")
for i in range(len(n)):

    print(n[i])

print("elelment in matrics wise:-")
for i in range(len(n)):
  for j in range(len(n[i])):
      print(n[i][j],end=" ")
  print()