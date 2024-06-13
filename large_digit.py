n=12543
large=n%10
while n>0:
    rem=n%10
    if rem>large:

        large=rem
    n=n//10
print(large)
