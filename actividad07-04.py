import pandas as pd

df=pd.read_csv("StudentsPerformance.csv")


print(df[["gender","reading score","writing score"]].tail(3)) # muesra una columna
print(df.iloc[:, -3: ])
print(df.head(100))
print(df.mean)
print(df.min)
print(df.max)
print(f'cantidad: "{df.shape}')
print(df.to_string())
