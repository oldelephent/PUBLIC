"""
First solution
import time

for i in range(11):
    print(f"Count: {i}", end="\r")
    time.sleep(1)

"""

# Second not working 10 90 80 70 60 50 
import time

for i in range(10, 0, -1):
    print(f"Count: {i}", end="\r")
    time.sleep(1)
print("Done!          ")  # To clear the last count



"""
3rd 10 9 8 7 6 5 4 
import time

for i in range(10, 0, -1):
    print(f"Count: {i}  ", end="\r")
    time.sleep(1)
print("Done!          ")  # To clear the last count

"""