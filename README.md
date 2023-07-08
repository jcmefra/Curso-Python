# Curso-Python PIP
Repositorio realizado en el curso de Python: PIP y entornos virtuales

# Requerimientos
Tener instalado Python en tu consola o en un intérprete como VSC

# Game 

Para correr el juego debes seguir las siguientes instrucciones en la terminal:

```sh
cd game
python3 Jankenpo.py
```

# Population

```sh
cd population
code . #Solo si tienes VSC, debes tener instalado Pandas, matplotlib y Numpy
```
Ejecutas el código Population.py siguiendo sus directrices de selección de país y continente.

Ahora, si no tienes VSC y quieres ejecutar desde el terminal:

```sh
sudo apt-get install python3-tk 
#pip install pyqt5 #puede ser una alternativa al GUI backend de la línea anterior.
#NO usar ambas GUI backend al mismo tiempo.
cd population
#python3 -m venv /path/to/new/virtual/environment (si quieres crear un nuevo virtual environment)
#source <venv>/bin/activate
pip install -r requirements.txt
python3 Population.py
```