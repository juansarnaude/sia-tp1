# Grupo 4 SIA

Gastón Alasia, 61413
Juan Segundo Arnaude, 62184
Bautista Canevaro, 62179
Matías Wodtke, 62098

Required:
* python
* pygame
* numpy
* pandas
* plotly

## ./main.py : 

Programa para encontrar soluciones e informacion de algoritmmos de busqueda de soluciones para el juego Sokoban.

python ./main.py {level_path}

El level_path es el path a un archivo de nivel de Sokoban. En la carpeta maps se pueden ver ejemplos de este tipo de mapas.

En este formato de mapas:
* '#' es una pared
* '$' es una caja
* '.' es un goal
* '*' es una caja sobre un goal
* '@' es el personaje


Las configuraciones y parametros de ./main.py configura desde ./configs/config.json

Este archivo debe ser un .json con los siguientes atributos:
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
* "iteration_count": numero de veces que queremos correr el programa.
* "output_file_name"
* "iddfs_limit": solo utilizadk cuando el algoritmo es iddfs, es el limite de profundidad en dicho algoritmo.

Aqui un ejemplo:
{
    "algorithm": "iddfs",
    "heuristics": ["euclidean_non_admissible", "box_stuck"],
    "iteration_count": 4,
    "output_file_name":"results/uninformed/lv1.txt-2.json",
    "iddfs_limit":40
}

El output de la ejecuccion sera un JSON con los siguientes valores de salida:
* "status": es 'success' si se pdo encontrar una solucion, sino es 'failure'.
* "solution": lista de las soluciones encontradas en todas las iteraciones.
* "execution_time": lista del tiempo que tardo en ejecutar cada iteracion.
* "explored_node_count": lista de cantidad de nodos explorados en cada iteracion.
* "frontier_node_count": lista de cantidad de nodos en la frontera al momento de enoctrar la solucion en cada iteracion.
* "initial_map": representacion del mapa de Sokoban utilizado.
* "algorithm": algoritmo utilizado.
* "heuristics": lista de la heuristicas utilizadas.

## ./create_animation.py

Programa para crear una animacion de la solucion encontrada por ./main.py.

python create_animation.py {solution_path}

Donde {solution_path} es el path a la solucion retornada cuando se ejecuto el ./mian.py 


