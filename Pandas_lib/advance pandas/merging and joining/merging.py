import pandas as pd

df_cust=pd.DataFrame({
    'cust_id': [1, 2, 3],
    'cust_name': ['Alice', 'Bob', 'Charlie']
})

df_order=pd.DataFrame({
    'cust_id':[1,2,4],
    'order_amt':[250,400,100]
})

df_merged=pd.merge(df_cust, df_order, on='cust_id',how='inner')
print("inner join")
print(df_merged)

df_merged=pd.merge(df_cust, df_order, on='cust_id',how='outer')
print("outer join")
print(df_merged)

df_merged=pd.merge(df_cust, df_order, on='cust_id',how='left')
print("left join")
print(df_merged)

df_merged=pd.merge(df_cust, df_order, on='cust_id',how='right')
print("right join")
print(df_merged)

# df_merged=pd.merge(df_cust, df_order, on='cust_id',how='cross')
# print("cross join")
# print(df_merged)