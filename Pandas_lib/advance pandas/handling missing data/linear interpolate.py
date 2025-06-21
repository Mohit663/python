import pandas as pd

df=pd.DataFrame({
    'time':[1,2,3,4,5],
    'value':[100,None,300,None,500]
})

print('before interpolation')
print(df)

df['value']=df['value'].interpolate(method='linear')
print('after interpolation')
print(df)