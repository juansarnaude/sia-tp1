import pandas as pd
import json
import plotly.express as px
import numpy as np

# Cargar configuración
with open("configs/config_dataset_iddfs.json", 'r') as file:
    config = json.load(file)
    map = config["map"]
    iddfs_limits = config["iddfs_limits"]
    iterations = config["iteration_count"]

# Inicializar listas para métricas
mean_execution_time = []
std_execution_time = []
every_solution_length = []
every_explored_nodes_count = []

# Cargar resultados para cada límite de IDDFS
for limit in iddfs_limits:
    with open(f"results/iddfs_limits/{map.split('/')[1].split('.')[0]}.txt-{limit}.json", 'r') as data_file:
        data = json.load(data_file)
        execution_time = data["execution_time"]
        solution_length = data["solution_length"]
        explored_nodes_count = data["explored_nodes_count"]

        # Calcular métricas
        mean_execution_time.append(np.mean(execution_time))
        std_execution_time.append(np.std(execution_time))
        every_solution_length.append(solution_length[0])
        every_explored_nodes_count.append(explored_nodes_count[0])

# Crear y mostrar gráficos

# Gráfico de Tiempo de Ejecución
df1 = pd.DataFrame({
    "IDDFS Limit": iddfs_limits,
    "Execution Time": mean_execution_time,
})
fig1 = px.bar(df1, x="IDDFS Limit", y="Execution Time", color="IDDFS Limit",
              title=f"Execution Time Across IDDFS Limits - Level {map.split('/')[1].split('.')[0]}",
              error_y=std_execution_time)

fig1.update_layout(
    font=dict(size=32),
    title=dict(font=dict(size=32)),
    xaxis=dict(
        title_font=dict(size=24),
        tickfont=dict(size=20),
        tickvals=iddfs_limits  # Mostrar solo los valores de IDDFS Limits
    ),
    yaxis=dict(title_font=dict(size=24), tickfont=dict(size=20)),
    legend=dict(font=dict(size=20))
)

fig1.show()

# Gráfico de Longitud de Solución
df2 = pd.DataFrame({
    "IDDFS Limit": iddfs_limits,
    "Steps to solution": every_solution_length,
})
fig2 = px.bar(df2, x="IDDFS Limit", y="Steps to solution", color="IDDFS Limit",
              title=f"Optimality of Solutions Across IDDFS Limits - Level {map.split('/')[1].split('.')[0]}")

fig2.update_layout(
    font=dict(size=32),
    title=dict(font=dict(size=32)),
    xaxis=dict(
        title_font=dict(size=24),
        tickfont=dict(size=20),
        tickvals=iddfs_limits  # Mostrar solo los valores de IDDFS Limits
    ),
    yaxis=dict(title_font=dict(size=24), tickfont=dict(size=20)),
    legend=dict(font=dict(size=20))
)

fig2.show()

# Gráfico de Conteo de Nodos Explorados
df3 = pd.DataFrame({
    "IDDFS Limit": iddfs_limits,
    "Explored nodes count": every_explored_nodes_count,
})
fig3 = px.bar(df3, x="IDDFS Limit", y="Explored nodes count", color="IDDFS Limit",
              title=f"Explored Nodes Count Across IDDFS Limits - Level {map.split('/')[1].split('.')[0]}")

fig3.update_layout(
    font=dict(size=32),
    title=dict(font=dict(size=32)),
    xaxis=dict(
        title_font=dict(size=24),
        tickfont=dict(size=20),
        tickvals=iddfs_limits  # Mostrar solo los valores de IDDFS Limits
    ),
    yaxis=dict(title_font=dict(size=24), tickfont=dict(size=20)),
    legend=dict(font=dict(size=20))
)

fig3.show()
