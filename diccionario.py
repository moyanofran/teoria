import pandas as pd

provincia=["cordoba ","bs as", "jujuy", "corrientes"]

poblacion=[10000,10001,2,3000]

"diccionario"

diccionario={"Provincia":provincia,"Poblacion":poblacion}

df=pd.DataFrame(diccionario)

print(df)