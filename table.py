from random import randint
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

i_time = []
a_time = [0]
print('\n')
print('Customer No\t\tInterarrival Time\t\tArrival Time on Clock')
for i in range(5):
    i_time.append(randint(1,10))
for r in range(1,len(i_time)+1):
    if r==1:
        print(f'\t{r}\t\t\t0\t\t\t\t{a_time[r-1]}')
    else:
        a_time.append(i_time[r-1]+a_time[r-2])
        print(f'\t{r}\t\t\t{i_time[r-1]}\t\t\t\t{a_time[r-1]}')
        
plt.hist(i_time)
