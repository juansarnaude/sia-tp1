import json
import os
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Ruta al directorio que contiene los archivos JSON
directory = 'results/uninformed/'

# Inicializamos un set para almacenar los niveles
levels = set()
algorithms = ['bfs', 'dfs', 'iddfs']
explored_nodes = {}

# Recorremos los archivos en el directorio para detectar los niveles y sumar nodos explorados
for file_name in os.listdir(directory):
    if file_name.endswith('.json'):
        level = file_name.split('-')[0]  # Extrae el nombre del nivel (parte antes del guion)
        levels.add(level)  # Añade el nivel al conjunto de niveles únicos
        if level not in explored_nodes:
            explored_nodes[level] = {algo: 0 for algo in algorithms}

        file_path = os.path.join(directory, file_name)

        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            algo = data['algorithm']
            explored_nodes[level][algo] += data['explored_nodes_count'][0]  # Sumamos los nodos explorados

# Convertimos el set de niveles a una lista y lo ordenamos
levels = sorted(list(levels))

# Creamos el gráfico de barras con Plotly
fig = make_subplots(rows=1, cols=1)

for algo in algorithms:
    fig.add_trace(go.Bar(
        x=levels,
        y=[explored_nodes[level][algo] for level in levels],
        name=algo,
        text_auto=True
    ))

# Configuramos el diseño del gráfico
fig.update_layout(
    title="Explored Nodes by Uninformed Algorithms per Level",
    xaxis_title="Levels",
    yaxis_title="Explored Nodes",
    barmode='group'
)

# Mostramos el gráfico
fig.show()
