#plt.scatter(x,y, color='color name', marker='marker style', label='label name')

import matplotlib.pyplot as plt

hours_studied = [1,2,3,4,5,6,7,8]
exam_scores = [50,55,60,65,70,75,80,85]

plt.scatter(hours_studied, exam_scores, color='pink', marker='s', label='student data')
plt.xlabel('Hours studied')
plt.ylabel('Exam score')
plt.title('Relationship between study time and exam score')
plt.legend()
plt.grid(True)
plt.show()