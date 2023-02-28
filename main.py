import random
import math
import time

print(' Welcome to Python... '.center(60))
print('Here is numbers generated which has a number missing within it.\n')
print('You have to guess the correct number...\n')
num=math.floor(random.random()*50);
# print(num)
for i in range(1,51):
  if i==num:
    pass
  else:
    print(i)

time.sleep(1)
print("Enter your guess....\n")
guess=int(input())
if(guess==num):
  print("Congratulations....! You are champion and keen observation....!\n")
else:
  print(" Sorry try next time\n")
  time.sleep(2)
  print("Good....Bye!")