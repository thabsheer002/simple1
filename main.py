import os
file = input("enter the file to be opened")
if "d"in file or "D"in file:
    os.startfile("D:")
elif "c" in file or "C"in file :
    os.startfile("C:")