import pandas as pd
df=pd.read_csv('sales_data_sample.csv', encoding='latin1')
df1=df.info()
print(df1)