# Grupo 4 SIA - 2C | 2024

### Integrantes

Gastón Alasia, 61413\
Juan Segundo Arnaude, 62184\
Bautista Canevaro, 62179\
Matías Wodtke, 62098\

# Sokoban

### Librerías de python requeridas
* pygame
* numpy
* pandas
* plotly

### Versión de python recomendada
V3.10.13

## Instalación
Puede configurarse este proyecto instalando las librerías previamente listadas usando pip, si se quiere realizar la instalación en su máquina, o en Anaconda, para una instalación en un entorno virtual.

### pip
Si aún no cuenta con pip puede instalarlo haciendo click [aquí](https://pip.pypa.io/en/stable/installation/).\
Para instalar las librerías usando pip simplemente ejecutamos en una terminal:
```bash
pip install pygame numpy pandas plotly
```

### Anaconda
Si aún no cuenta con Anaconda puede instalarlo haciendo click [aquí](https://www.anaconda.com/download/success).\
Si se quiere crear un entorno virtual debe ejecutarse en una terminal:
```bash
conda create --name [environment_name]
```
Donde se completa [environment_name] con el nombre que se quiere establecer para el entorno virtual.\
A continuación activamos el entorno virtual usando el comando:
```bash
conda activate [environment_name]
```
Debe utilizarse el mismo nombre de entorno que se utilizó en el paso anterior.\
Luego para instalar las librerías en el entorno virual usando Anaconda simplemente ejecutamos:
```bash
conda install pygame numpy pandas plotly
```

## Ejecución del juego 

Una vez terminada la instalación puede ejecutarse el programa para encontrar soluciones e información de algoritmmos de búsqueda de soluciones para el juego Sokoban.

Para ejecutarlo utilizamos:
```bash
python ./main.py {level_path}
```
Donde level_path es el path a un archivo de nivel de Sokoban. En la carpeta 'maps' se pueden ver ejemplos de este tipo de mapas.

Podemos establecer parametros para la ejecucion de main.py en el archivo ubicado en '/configs/config.json'

Este archivo es un JSON con los siguientes atributos:
* "algorithm" : el algoritmo que deseamos utilizar par obtener la solucion al nivel. Las opciones son:
  * "a_star"
  * "bfs"
  * "dfs"
  * "global_greedy"
  * "local_greedy"
  * "iddfs"
* "heuristics": una lista de las heuristicas a utilizar, las opciones son las siguientes:
  * "box_stuck"
  * "boxes_in_goals"
  * "euclidean"
  * "euclidean_non_admissible"
  * "manhattan"
  * "manhattan_non_admissible"
  Donde box_stuck puede utilizarse junto con cualquiera de las demás heurísticas
* "iteration_count": numero de veces que queremos correr el programa.
* "output_file_name": Debe configurarse el path del archivo creado a partir de directorios existentes.
* "iddfs_limit": solo es utilizado cuando el algoritmo es iddfs, es el limite de profundidad en dicho algoritmo.

### Ejemplo de archivo config.json
```json
{
    "algorithm": "iddfs",
    "heuristics": ["euclidean_non_admissible", "box_stuck"],
    "iteration_count": 4,
    "output_file_name":"results/uninformed/lv5.json",
    "iddfs_limit":2
}
```

<span style="color:red">Tener en cuenta que los algoritmos de búsqueda desinformados no aplicarán ninguna heurística por más de que se la configure en el 'config.json'</span>.

El output de la ejecuccion sera un archivo JSON con los siguientes valores de salida:
* "status": 'success' si se pudo encontrar una solucion, 'failure' sino.
* "solution": lista de las soluciones encontradas en todas las iteraciones.
* "execution_time": lista del tiempo que tardo en ejecutar cada iteracion.
* "explored_node_count": lista de cantidad de nodos explorados en cada iteracion.
* "frontier_node_count": lista de cantidad de nodos en la frontera al momento de enoctrar la solucion en cada iteracion.
* "initial_map": representacion del mapa de Sokoban utilizado.
* "algorithm": algoritmo utilizado.
* "heuristics": lista de la heuristicas utilizadas.

### Ejemplo de salida
Para el archivo de configuración explicitado la salida es el siguiente archivo JSON
```json
{
     "status": "success",
     "solution": [
          "RRR",
          "RRR",
          "RRR"
     ],
     "solution_length": [
          3,
          3,
          3
     ],
     "iddfs_limit": [
          2,
          2,
          2
     ],
     "execution_time": [
          4.744529724121094e-05,
          2.8371810913085938e-05,
          2.6226043701171875e-05
     ],
     "explored_nodes_count": [
          3,
          3,
          3
     ],
     "frontier_node_counts": [
          1,
          1,
          1
     ],
     "initial_map": "#######\n#@ $ .#\n#######\n",
     "algorithm": "iddfs",
     "heuristic": [
          "euclidean_non_admissible",
          "box_stuck"
     ]
}
```

## Estructura de representación de mapas

Los mismos se encuentran definidos de la siguiente manera:
* '#' es una pared
* '$' es una caja
* '.' es un objetivo
* '*' es una caja sobre un objetivo
* '@' es el personaje
* '+' es el personaje sobre un objetivo

Se sugiere añadir niveles nuevos 

## Visualización

Para visualizar la solución de un nivel el cual hayamos ejecutado utilizando el archivo 'main.py' debemos ejecutar desde el directorio raíz:
```bash
python create_animation.py [result_file_path]
```
Donde <span style="color:orange">result_file_path</span> será un archivo de resultados en formato JSON el cual se sugiere almacenar en el directorio 'results' en la carpeta raíz del proyecto.

## Experimentos y análisis de datos
En el directorio 'plot' encontrará todo lo necesario para realizar los experimentos y para evaluar los resultados. Dentro de este existen otros dos directorios llamados 'DataSetGenerators', para generar los archivos de resultados, y 'Plotting', donde se encuentran los archivos de python que generan los gráficos


