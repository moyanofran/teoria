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

#crear uan columna con numeros
import pandas as pd
import numpy as np

df=pd.read_csv('StudentsPerfonmance.csv')

a=np.random.randit(1,100,size=1000)

df['columna de arreglo'] = a

print(df)
# crea con numeros decimales
import pandas as pd
import numpy as np

df=pd.read_csv('StudentsPerfonmance.csv')

a=np.random.uniform(1,100,size=1000)

df['columna de arreglo'] = a

print(df)













#crear una columna con numeros
import pandas as pd

df=pd.read_csv('StudentsPerfonmance.csv')
print(df["math score"].sum)# .sum (suma)
print(df.head)

#actividad 2
import pandas as pd

df=pd.read_csv('StudentsPerfonmance.csv')
print(df["math score"].count)# .count (cuenta)
print(df.head)

#actividad 3

df=pd.read_csv('StudentsPerfonmance.csv')
print(df["math score"].median)# .median (media)
print(df.head)

#actividad 4

df=pd.read_csv('StudentsPerfonmance.csv')
print(df["math score"].std)# .std (moda)
print(df.head)

#actividad 5

df=pd.read_csv('StudentsPerfonmance.csv')
print(df["math score"].max)# .max (maximo)
print(df.head)

#actividad 6

df=pd.read_csv('StudentsPerfonmance.csv')
print(df["math score"].min)# .min (mimnimo)
print(df.head)








#sumar la fila de varias columnas
import pandas as pd
df=pd.read_csv('StudentsPerfonmance.csv')
print(df["math score"]+df['reading score']+df['writing score'])

#












