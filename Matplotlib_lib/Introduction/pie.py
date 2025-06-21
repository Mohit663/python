#plt.pie(values, labels=label_list, color='color', autopct ='%1.1f%%')

import matplotlib.pyplot as plt
regions = ['North','South','East','West']
revenue = [3000,2000,1500,1000]

plt.pie(revenue, labels=regions, autopct='%1.1f%%', colors = ['green','gold','coral','orange'])
plt.title("revenue contribution by region")
plt.show()

