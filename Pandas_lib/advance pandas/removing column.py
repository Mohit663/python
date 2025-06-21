import pandas as pd
df = pd.DataFrame({'Name': ['Mohit', 'Avinash', 'Mayank'], 'Age': [21, 21, 20], 'city': ['Jaipur', 'Alwar', 'Jaipur']})
print(df)

# # df.drop(columns=['column_name], inplace=True)
# # single column
df.drop(columns=['city'], inplace=True)
print(df)

# df.drop(columns=['column_name1','column_name2'], inplace=True)
# multiple columns
df.drop(columns=['Age','city'], inplace=True)
print(df)