#crear columna nueva
import pandas as pd
df=pd.read_csv('StudentsPerformance.csv')

df["nueva columna"] = 70

print(df)

#actividad 2 crear una columna a traves de un arreglo
import numpy as np
import pandas as pd
a=np.arange(0,1000)

df['columna de arreglo'] = a
print=df

