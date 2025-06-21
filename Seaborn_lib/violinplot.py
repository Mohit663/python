import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = sns.load_dataset("titanic")
print(data)

sns.violinplot(x='pclass',y='fare', data= data, palette = ['red','green','blue'], hue='sex')
plt.show()