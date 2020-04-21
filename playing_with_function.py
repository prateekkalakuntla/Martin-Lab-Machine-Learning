import tensorflow as tf
import numpy as np
import random
import matplotlib.pyplot as plt

x = 1
y = 1
final_x = []
final_y = []
for i in range(100):
    x = 1.14*x
    final_x.append(x)
    y = 1.14*(y+10)
    final_y.append(y)

# plt.figure()
# plt.plot([i for i in range(100)], final_x)
# plt.plot([i for i in range(100)], final_y)
# plt.show()
# plt.close()

final_value = final_x[99]
print(final_value)
for i in range(len(final_y)):
    if final_value < final_y[i]:
        print(i)
        break