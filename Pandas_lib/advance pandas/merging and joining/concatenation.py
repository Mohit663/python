import pandas as pd

df_R1=pd.DataFrame({
    'cust_id': [1, 2, 3],
    'cust_name': ['Alice', 'Bob', 'Charlie']
})

df_R2=pd.DataFrame({
    'cust_id': [4, 5, 6],
    'cust_name': ['Mohit', 'Mayank', 'Avinash']
})

# vertically
df_concatenated=pd.concat([df_R1,df_R2],ignore_index=True)
print(df_concatenated)

# horizontally
df_concatenated=pd.concat([df_R1,df_R2],axis=1,ignore_index=True)
print(df_concatenated)