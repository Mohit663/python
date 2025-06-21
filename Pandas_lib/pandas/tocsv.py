import pandas as pd
df = pd.DataFrame({'Name': ['Mohit', 'Avinash', 'Mayank'], 'Age': [21, 21, 20], 'city': ['Jaipur', 'Alwar', 'Jaipur']})
df.to_csv('output.csv', index=False)
print(df)