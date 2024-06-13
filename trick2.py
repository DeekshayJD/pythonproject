'''

Write a program to read 100 log files and provide a test result summary
file1.log: PASS 5; FAIL - 5
file2.log: PASS 10;FAIL - 0
file3.log: PASS 0; FAIL - 10
'''
import os
for i in range(1,100):
    #file_name = f"file{i + 1}.log"
    file_name = f"newfile{i + 1}"
    with open(file_name,"w")as fo:
        fo.write("good morning")

    #file_name=file_name{i+1}
    with open(file_name,"r")as fo:
        print(fo.read())
    os.remove(file_name)


