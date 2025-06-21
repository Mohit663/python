import pandas as pd
df = pd.DataFrame({'Name': ['Mohit', 'Avinash', 'Mayank'], 'Age': [21, 21, 20], 'city': ['Jaipur', 'Alwar', 'Jaipur']})
print('Sample Dataframe : ')
print(df)

# filtering rows using single condition
print('filtering rows using single condition')
high_age=df[df['Age']>20]
print(high_age)

# filtering rows using multiple conditions
print('filtering rows using multiple conditions')
filtered=df[(df['Age']>20) & (df['city']=='Jaipur')]
print(filtered)