import pandas as pd

df=pd.read_csv("StudentsPerformance.csv")

print(df.head()) #mostrar cabeza

print(df.teil(20)) #mostrar pie

print(df.to_string()) #muestra todo

print(df.shape) #tira dos numeros, cantidadde filas y columnas

print(df.dtypes) #mostrar ostipos de dato

print(df.info()) #muestra datos sin completar ( no null), para limpiar

print-(df.describe()) #da datos estadisticos de la tabla

print(df[["gender","maxcore"]].head()) # muesra una columna
