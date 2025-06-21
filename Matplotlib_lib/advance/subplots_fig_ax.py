#fig, ax = plt.subplots(nrows, ncols, figsize=(width, height))


import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,2, figsize = (10,5))

x = [1,2,3,4]
y = [10,20,15,25]

ax[0].plot(x,y,color='orange')
ax[0].set_title('Line Plot')

ax[1].bar(x,y,color='pink')
ax[1].set_title('Bar Chart')

fig.suptitle('Comparison of line and bar charts')

plt.show()