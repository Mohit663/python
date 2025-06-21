#sns.lineplot(x='value',y='value',data=data,hue='value',size=size,style='style_value',palette='color combination')

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = sns.load_dataset("penguins")
data1 = pd.DataFrame(data)
print(data)

sns.lineplot(x='bill_length_mm',y='bill_depth_mm',data=data1,hue='sex',size=10,style='sex',palette='Accent',markers=['o','>'])
plt.show()