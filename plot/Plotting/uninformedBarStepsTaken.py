import json
import os
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Ruta al directorio que contiene los archivos JSON
directory = 'results/uninformed/'

# Detección automática de niveles
levels = set()
algorithms = ['bfs', 'dfs', 'iddfs']
solution_lengths = {}

# Recorremos los archivos en el directorio
for file_name in os.listdir(directory):
    if file_name.endswith('.json'):
        level = file_name.split('-')[0]  # Extrae el nombre del nivel (parte antes del guión)
        levels.add(level)  # Añade el nivel a la lista de niveles únicos
        if level not in solution_lengths:
            solution_lengths[level] = {algo: 0 for algo in algorithms}

        file_path = os.path.join(directory, file_name)

        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            algo = data['algorithm']
            solution_lengths[level][algo] += data['solution_length'][0]  # Sumamos la longitud de la solución

# Ordenamos los niveles para que aparezcan en orden en el gráfico
levels = sorted(list(levels))

# Creamos el gráfico de barras con Plotly
fig = make_subplots(rows=1, cols=1)

for algo in algorithms:
    fig.add_trace(go.Bar(
        x=levels,
        y=[solution_lengths[level][algo] for level in levels],
        name=algo
    ))

# Configuramos el diseño del gráfico
fig.update_layout(
    title="Steps Taken by Uninformed Algorithms per Level",
    xaxis_title="Levels",
    yaxis_title="Steps",
    barmode='group'
)

# Mostramos el gráfico
fig.show()
