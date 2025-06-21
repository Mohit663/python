import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = sns.load_dataset("titanic")
print(data)

sns.pairplot(data[['pclass','fare','age','sibsp']],hue='sibsp')
plt.show()