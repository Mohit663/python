import pandas as pd
df = pd.DataFrame({'Name': ['Mohit', 'Avinash', 'Mayank'], 'Age': [21, 21, 20], 'city': ['Jaipur', 'Alwar', 'Jaipur']})
print(df)

# using .loc
# df.loc[row_index,'Column_name']=new_value

df.loc[2,'Age'] = 22
print(df)