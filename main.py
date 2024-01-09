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
  new_speed[i]=Random.randint(1,121)