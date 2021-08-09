#visualizations
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

height = [110,140,150,160,170]
weight = [30,40,50,60,70]
calories_burnt = [60,70,75,80]

plt.plot(height, weight)
plt.title("Height Weight Relationship")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()

#add legends
plt.plot(calories_burnt)
plt.plot(weight)
plt.legend(labels=['Calories Burnt','Weight'],loc='lower right')
#set labels for x axis units
plt.xticks(ticks=[0,1,2,3], labels=['p1','p2','p3','p4'])
plt.show()
