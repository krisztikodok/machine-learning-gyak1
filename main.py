import numpy  #mean,median
from scipy import stats  #mode
import random
import math  #sqr

speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = numpy.mean(speed)  #avg
y = numpy.median(speed)
z = stats.mode(speed)
print(f"Mean: {x}\tMedian: {y}\t {z}")

new_speed = []
for i in range(10):
  k = random.randint(1, 121)
  new_speed.append(k)

print(new_speed)
a = numpy.std(speed)
b = numpy.std(new_speed)  #standard deviation
print(f"Std. deviation of 'speed': {a:.2f}")
print(f"Std. deviation of 'new_speed': {b:.2f}")

print("\n\n")
distances = [210, 20014, 3101, 979, 32000, 400]
c = numpy.var(distances)  #variance (sqr of std. dev)
print(distances)
d = numpy.std(distances)
print(f"Standard deviance of distances: {d:.4f}")
print(f"Variance of distances: {c:.4f}")
variance_root = math.sqrt(c)
if d == variance_root:
  print("Correct")
else:
  print("Something's wrong")

print("\n\n")
#percentile
speed_perc = numpy.percentile(speed, 100)
new_speed_perc = numpy.percentile(new_speed, 100)
print(f"Speed percentile:{speed_perc}\nNew speed percentile:{new_speed_perc}")
