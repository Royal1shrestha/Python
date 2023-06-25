import threading
import time

def wake_up():
    time.sleep(2)
    print("You are awake.")
    
def drink_tea():
    time.sleep(3)
    print("I drank tea.")
    
x = threading.Thread(target=wake_up,args=()) #Put arguments of function if there in args=
x.start()

y = threading.Thread(target=drink_tea,args=()) #Put arguments of function if there in args=
y.start()

# to execute threads before main thread use join
x.join()
y.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

def timer():
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged time : ",count)
        
x = threading.Thread(target=timer,daemon=True)
x.start()

answer = input("Do you want to exit?")