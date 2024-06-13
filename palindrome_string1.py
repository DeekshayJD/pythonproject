
def check_palin (str):

      for i in range (0, int (len (str)/2)):

                     if str [i] != str [len (str) -i-1]:

                                    return False

                     return True

str_1 =input("enter string:-")

ans = check_palin (str_1)

if (ans):

   print("palindrom")

else:
 print("not palindrom")