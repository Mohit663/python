#savefig('filename.extension', dpi = value, bbox_inches = 'tight')

import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [10,20,15,25]

plt.plot(x,y,color='blue',marker='s')
plt.title('Simple line plot')
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.savefig("line_plot.png", dpi=300, bbox_inches='tight')
plt.show()