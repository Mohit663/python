import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = sns.load_dataset("titanic")
print(data)

sns.scatterplot(x='age',y='fare',data=data, palette = ['red','green','black'], hue = 'class', size ='pclass')
plt.show()