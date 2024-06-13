import os

# Print current working directory
print("Current working directory:", os.getcwd())

# Change working directory to a new location
os.chdir(r"C:\Users\ddevraj\PycharmProjects\pythonProject\python_QA")

# Print new current working directory
print("New working directory:", os.getcwd())
for i in os.listdir():
    print(i)