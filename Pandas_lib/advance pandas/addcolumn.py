import pandas as pd
df = pd.DataFrame({'Name': ['Mohit', 'Avinash', 'Mayank'], 'Age': [21, 21, 20], 'city': ['Jaipur', 'Alwar', 'Jaipur']})
print(df)

df["mobile"] = [8107529091,8619721248,6375869777]
print(df)

# using insert method
df.insert(3,'email',['mohitaga663@gmail.com','avinashgoyal12@gmail.com','jainmayankrajawas@gmail.com'])
print(df)