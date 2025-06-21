import pandas as pd

df=pd.DataFrame({
    'Name':['Mohit','Avinash','Mayank'],
    'Age':[21,20,22],
    'Salary':[20000,12000,25000]
})

print('Before Sorting')
print(df)
 
df.sort_values(by=['Age','Salary'], ascending=[False,True], inplace=True)
print('After Sorting')
print(df)