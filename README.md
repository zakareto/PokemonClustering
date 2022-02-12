<p align="center">
<a href="https://github.com/zakareto"><img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Pok%C3%A9_Ball_icon.svg/640px-Pok%C3%A9_Ball_icon.svg.png" width = 100> </a>
</p>
<h1 align=center><font size = 5>Machine Learning para categorizar a los Pókemon.</font></h1>
<br>

# Justificación del proyecto
<br>


Este es un pequeño ejercicio con el objetivo de entender el algoritmo de K-means para agrupamiento de datos.

Decidí utilizar una base de datos sobre las estadísticas de los Pokémon. Me considero muy fanático de la saga, así que se me hace una idea interesante analizar los datos que contienen.



<br>

***
# Data
<br>

Para este trabajo utilicé la base de datos de <a href="https://www.kaggle.com/thiagoazen/all-pokemon-with-stats/version/1">"All Pokemon with Stats"</a> creada por el usuario  <a href="https://www.kaggle.com/thiagoazen">ThiagoAzen</a> en la plataforma de Kaggle.

Las características de la colección de datos son las siguientes:

- Name: El nombre del Pokémon
- Variation: Si es una forma alternativa de otro Pokémon (forma regional, megaevolución, etc)
- Type1: El tipo primario del Pokémon
- Type2: Algunos Pokémon pueden tener un tipo secundario, representado en esta columna
- Total: la suma de los valores de cada estadística del Pokémon
- HP: los puntos de vida maximos del Pókemon
- Attack: los puntos de ataque maximos del Pókemon
- Defense: los puntos de defensa maximos del Pókemon
- Sp.Atak: los puntos de ataque especial maximos del Pókemon
- Sp.Def: los puntos de defensa especial maximos del Pókemon
- Speed: los puntos de velocidad maximos del Pókemon
<br>

***
# Metodología
<br>

El lenguaje utilizado es el de Python. Para falicitar la prueba y visualización deje dos versiones del proyecto, uno en ".py" y otro como un archivo de libreta jupyter, para poder usar el que se te haga mas cómodo.
Tambien se usaron las librerias de Pandas y Scikit-Learn para poder ejecutar el algoritmo y la obtención de los resultados.

Para poder trabajar con Scikit-Learn solo hay que seguir los siguientes pasos:

1 - Importar las librerías que necesitaremos.
2 - Seleccionar nuestro documento de entrada para el set de datos.
3 - crear un dataframe con los datos del documento.
4 - Seleccionar los nombres de la columna que no usaremos. para este analisis se descartan los valores del nombre, variaciones y tipos.
5 - Definir el número de grupos con el parámetro "n_clusters", en este caso definimos 6.
6 - Incrustar nuestra predicción en el set de datos usando una columna con el nombre "grupo".
7 - Exportar los resultados a un archivo en la carpeta deseada.

Los archivos tienen tambien unas líneas para presentar el texto de forma ordenada en la terminal al finalizar la ejecución. Esto es un extra para poder visualizar la información rapidamente sin tener que abrir el archivo exportado.

***
 # Conclusión<br>
Al finalizar la ejecución del algoritmo se puede notar que los grupos creados se basan en un rango de valores de la columna total, agrupandolos en 6 grupos segun que tan bajo o alto sean. 

Se puede notar que los Pokémon con un total mas alto son los Pokémon legendarios (Mewtwo, Rayquaza, Eternatus) y las Megaevoluciones de algunos Pokémon dificiles de conseguir (Tyranitar y Metagross), con un rango de entre 680-1125

Los de la categoria mas baja tienden a ser las primeras etapas de familias de Pokémon de tipo bicho, o de familias con 3 etapas evolutivas consecutivas, con un rango de entre 170-300, con 352 Pokémon.

La categoria mas extensa es de los Pokémon que están en el rango de 480-550, Siendo en su mayoria las etapas finales de alguna familía evolutiva. Mientras que la menos extensa es la del rango de 680-1125, con menos de 60 Pokémon.

Este ejercició se podria utilizar también para obtener otros datos, como la relación de las estadisticas con los tipos elementales de los Pókemon.

<br>

***
# Inspiración
<br>
Este proyecto fue basado en un proyecto creado por el profesor <a href="https://www.linkedin.com/in/novelo-luis/">Luis Jorge Novelo Novelo</a> en su repositorio de GitHub <a href="https://github.com/PhinanceScientist/Candy-Clustering">"Candy-Clustering"</a>.<br>

<br>

***
# Librerias
<br>
  
   <li> <b>joblib:</b>   1.0.1<br></li>
   <li> <b>numpy </b> 1.21.0<br></li>
   <li> <b>pandas:</b> 1.3.0<br></li>   
   <li> <b>scikit-learn:</b> 0.24.2<br></li>
   <li> <b>scipy:</b> 1.7.0 <br></li>
  <br>

***
