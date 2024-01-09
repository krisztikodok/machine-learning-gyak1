import numpy #mean,median
from scipy import stats #mode
import random

speed=[1,2,3,4,5,6,7,8,9,10]
x=numpy.mean(speed) #avg
y=numpy.median(speed)
z=stats.mode(speed)
print(f"Mean: {x}\tMedian: {y}\t {z}")

new_speed=[]
for i in range(10):
  k=random.randint(1,121)
  new_speed.append(k)

print(new_speed)
a=numpy.std(speed)
b=numpy.std(new_speed) #standard deviation
print(f"Std. deviation of 'speed': {a:.2f}")
print(f"Std. deviation of 'new_speed': {b:.2f}")

