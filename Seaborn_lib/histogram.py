import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = sns.load_dataset("titanic")
print(data)

sns.histplot(x='age', data= data,kde = True, bins=10)
plt.show()