import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = sns.load_dataset("titanic")
print(data)

sns.jointplot(x='age',y='fare', data= data, hue = 'sex', palette = ['red','green'],kind='kde', shade=True)
sns.jointplot(x='age',y='fare', data= data, palette = ['red','green'],kind='hex', shade=True, cmap='YlGnBu')
sns.jointplot(x='age',y='fare', data= data, palette = ['red','green'],kind='hex', cmap='YlGnBu')
plt.show()