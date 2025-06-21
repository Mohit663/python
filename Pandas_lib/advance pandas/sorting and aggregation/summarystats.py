import pandas as pd

df=pd.DataFrame({
    'Name':['Mohit','Avinash','Mayank'],
    'Age':[21,20,22],
    'Salary':[20000,12000,25000]
})

print(df)

avg_salary=df['Salary'].mean()
print(avg_salary)