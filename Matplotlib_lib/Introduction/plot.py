#plt.plot(x,y, color = 'color name', linestyle='line style', linewidth = value, marker = 'marker symbol', label = 'label name')
import matplotlib.pyplot as plt
months = [1,2,3,4]
sales = [1000,1500,1200,1800]

plt.plot(months,sales,color='blue', linestyle='--', linewidth = 2, marker = 'o', label = '2025 sales data')
plt.xlabel("Months")
plt.ylabel("Sales per month")
plt.title("Monthly Sales Data Report")
plt.legend(loc="upper left", fontsize=12)
plt.grid(color = 'grey', linestyle=':', linewidth=1)
plt.xlim(1,4)
plt.ylim(0,2000)
plt.xticks([1,2,3,4],['M1','M2','M3','M4'])
plt.yticks([1000,1500,1200,1800],['S1','S2','S3','S4'])
plt.show()