# works only for numerical columns
# preserves data integrity
# smooth trends
# avoid data loss
# linear , polynomial , time

import pandas as pd

df = pd.DataFrame({
    'Name': ['Mohit', 'Avinash', 'Mayank','devanshu','aman'], 
    'Age': [21, None, 20,22,21], 
    'city': ['Jaipur', 'Alwar', 'Jaipur','Jaipur','Jaipur'],
    'salary': [20000, None, 30000, 15000, 15000]
    })

print(df)

df.interpolate(method="linear",axis=0,inplace=True)
print(df)