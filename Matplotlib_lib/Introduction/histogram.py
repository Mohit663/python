#plt.hist(data, bins=number_of_bins, color=colorname, edgecolor='black')

import matplotlib.pyplot as plt
scores = [45,67,89,56,78,88,92,60,74,81,59,66,75,82,90,95,70,73,68,67]
plt.hist(scores, bins=5, color='red', edgecolor='black')
plt.xlabel('score range')
plt.ylabel('number of student')
plt.title('score distribution of students')
plt.show()