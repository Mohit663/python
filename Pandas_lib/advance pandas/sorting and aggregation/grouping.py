import pandas as pd

df=pd.DataFrame({
    'Name':['Mohit','Avinash','Mayank','Devanshu','aman'],
    'Age':[21,20,22,22,21],
    'Salary':[20000,12000,25000,18000,20000]
})

print(df)

grouped=df.groupby('Age')['Salary'].sum()
print(grouped)