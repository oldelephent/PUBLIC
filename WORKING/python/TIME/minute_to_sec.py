import time
import datetime

#minutes in miliseconds
m = int(input("enter minute" ))
s = m*60000
while s >= 0:
    s -=1
    time.sleep(1)
    print(f"{m} minute in mili seconds {s}", end= "\r")


# #minites in seconds
# m = int(input("enter minute" ))
# s = m*60*60000
# while s >= 0:
#     s -=1
#     time.sleep(1)
#     print(f"{m} minute in seconds {s}", end= "\r")















