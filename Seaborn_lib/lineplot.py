import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

var = [1,2,3,4,5,6,7]
var1 = [2,3,4,1,5,6,7]

data = pd.DataFrame({'var':var, 'var1':var1})

sns.lineplot(data=data)
plt.show()