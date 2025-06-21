import pandas as pd
df = pd.DataFrame({'Name': ['Mohit', 'Avinash', 'Mayank'], 'Age': [21, 21, 20], 'city': ['Jaipur', 'Alwar', 'Jaipur']})
print('Sample Dataframe : ')
print(df)
print('Selecting one column : ')
print(df['Name'])
print('Selecting Multiple column : ')
subset = df[['Name','city']]
print(subset)