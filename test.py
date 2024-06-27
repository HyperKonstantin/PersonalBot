import random
import time
import datetime

def rand_num_generator():
    return random.randint(1, 100)

def number_sender():

    key = True
    while key:
        print("in cycle")
        key = False

    while True:
        time.sleep(3)
        num = rand_num_generator()
        yield num

# iter = number_sender()
# for i in range(5):
#     print(next(iter))

print(datetime.datetime.now())