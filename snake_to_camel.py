s="Bengaluru Is A Beutiful City"
words=s.split()
result=[word[0].lower()+word[1:].upper() for word in words ]
output=" ".join(result)
print(output)