import pandas as pd
df=pd.read_csv("Pandas_lib\pandas\sales_data_sample.csv", encoding='latin1')
print(df)
print('Top 10 rows are : ')
print(df.head(10))
print('Bottom 10 rows are : ')
print(df.tail(10))