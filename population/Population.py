import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.cm as cm

#Branch Main

df1 = pd.read_csv('data.csv') #Leer el CSV con Pandas
df2 = df1.set_index('Country/Territory', drop = False) #Definir columna índice o principal
lista_continentes = df1['Continent'].unique()
print ('Elija uno de los siguientes continentes: ' + ', '.join(lista_continentes))
while True:

    continente = input('Type continent name: ')
    df3 = df2[df2['Continent'] == continente] #Filtrar por continente
    if not df3.empty:
        world_ppl_per = df3['World Population Percentage'] #Extraer la columna que necesitamos

        labels = world_ppl_per.index.tolist() #Convertir el índice (países) a una lista
        sizes = world_ppl_per.tolist() #Convertir la columna World Population Percentage en una lista

        fig, ax = plt.subplots()

        # Asignar un color distinto a cada barra
        colormap = plt.cm.rainbow
        colors = colormap(np.linspace(0, 1, len(labels)))
        ax.bar(labels, sizes, color=colors)
        #ax.bar(labels, sizes)

        plt.title('Población mundial por país (%)')
        plt.xlabel('País', labelpad=10)
        plt.ylabel('Porcentaje de población')

        plt.xticks(rotation=90) #Rota 90 grados las etiquetas

        ax.tick_params(axis='x', labelsize=6.5)  # Ajusta el tamaño de fuente (8 es un ejemplo, ajusta según tus necesidades)

        # Ajustar los márgenes
        plt.subplots_adjust(bottom=0.35, left=0.12, right=0.95, top=0.9)  # Ajusta los valores según tus necesidades

        # Ajustar los límites del eje y
        ax.set_ylim(0, max(sizes) * 1.1)  # Ajusta el factor multiplicativo según tus necesidades

        plt.savefig('ppl_{}.png'.format(continente))
        plt.close()
        print("Graphic was generated and saved successfully")
        
        break

    else:
        print('Please write the continent name correctly')
        continue

