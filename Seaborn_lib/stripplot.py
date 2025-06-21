import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = sns.load_dataset("titanic")
print(data)

sns.stripplot(x='pclass',y='fare', data= data, palette = ['red','green'],dodge=True, hue='sex')
plt.show()