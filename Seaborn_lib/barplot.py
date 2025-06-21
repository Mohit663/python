import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = sns.load_dataset("titanic")
print(data)

sns.barplot(x='sex',y='fare', data= data)
plt.show()