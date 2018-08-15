import matplotlib.pyplot as plt
import numpy as np
import re

file = open("log.txt", "r") 

score = []
win_rate = []
iteration = []
for line in file:
     if re.search("2048", line) and re.search("%", line):
     	print(line)
     	win_rate.append(line.split('(')[1].split('%')[0])
        

     if re.search("mean", line):
     	print(line)
     	iteration.append(line.split("\tmean")[0])
     	score.append(line.split("mean = ")[1].split("\tmax")[0])


plt.figure(1)
plt.plot(iteration, score)
plt.title('TD-Learning for 2048 (Mean Score)')
plt.xlabel('Iteration')
plt.ylabel('Mean Score')
plt.savefig('mean.png')

plt.figure(2)
plt.plot(iteration, win_rate)
plt.title('TD-Learning for 2048 (Win Rate)')
plt.xlabel('Iteration')
plt.ylabel('Win Rate')
plt.savefig('win_rate.png')
plt.show()
