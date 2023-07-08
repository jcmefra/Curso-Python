import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df1 = pd.read_csv('./population/data.csv') #Leer el CSV con Pandas
df2 = df1.set_index('Country/Territory', drop = False) #Definir columna índice o principal
continente = input('Type continent name: ')

try:
    df3 = df2[df2['Continent'] == continente] #Filtrar por continente
    world_ppl_per = df3['World Population Percentage'] #Extraer la columna que necesitamos

    labels = world_ppl_per.index.tolist() #Convertir el índice (países) a una lista
    sizes = world_ppl_per.tolist() #Convertir la columna World Population Percentage en una lista

    fig, ax = plt.subplots()
    ax.pie(sizes, autopct='%1.1f%%')
    ax.axis('equal')
    ax.legend(labels=labels, loc = 'center left', ncol=2)
    plt.title('Población mundial por país (%)')
    plt.subplots_adjust(bottom=0.1, left = 0.1) #ajustar el margen para no cortar las labels
    fig.set_size_inches(19, 9.5)
    plt.savefig('ppl_{}.png'.format(continente))
    plt.close()

except KeyError as error:
    print('Please write the continent name correctly')