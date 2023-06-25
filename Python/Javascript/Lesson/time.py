import time

print(time.ctime(0)) #time when computer believes time started => epoch
print(time.time()) #time until epoch

print(time.ctime(time.time())) #real date and time