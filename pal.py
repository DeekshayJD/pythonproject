def palindrome(s):
   temp=s
   rev=0
   while s>0:
         rem = s % 10
         rev = rev * 10 + rem
         s = s // 10
   if temp==rev:
       print("palindrome")
   else:
       print("not palindrome")

s=121
palindrome(s)