#plt.scatter(x,y, color='color name', marker='marker style', label='label name')

import matplotlib.pyplot as plt


plt.scatter([1,2,3],[50,55,60], color='blue', label='class A')
plt.scatter([1,2,3],[45,50,52], color='orange', label='class B')
plt.xlabel('Hours studied')
plt.ylabel('Exam score')
plt.title('Comparison of two classes')
plt.legend()
plt.grid(True)
plt.show()