import os
import json
import pandas as pd
import plotly.express as px

directory = 'results/informedVsHeuristicsBoxStuck/'

# Cargar configuración
with open("configs/config_dataset.json", 'r') as file:
    config = json.load(file)
    heuristics = config["heuristics"]
    algorithms = config["algorithms"]
    map_name = config["map"].split('/')[-1].split('.')[0]  # Extraer el nombre del nivel dinámicamente

# Inicializar un DataFrame para almacenar los resultados
results_df = pd.DataFrame(columns=["Algorithm", "Heuristic", "Explored Nodes", "Box Stuck"])

# Procesar cada archivo JSON en el directorio
for filename in os.listdir(directory):
    if filename.endswith(".json") and filename.startswith(map_name):
        filepath = os.path.join(directory, filename)

        with open(filepath, 'r') as file:
            data = json.load(file)
            algorithm = data["algorithm"]
            explored_nodes = data["explored_nodes_count"][0]
            heuristic = ', '.join([h for h in data["heuristic"] if h != "box_stuck"])  # Eliminar 'box_stuck' del nombre

            # Verificar si el nombre del archivo contiene 'box_stuck'
            box_stuck = 'box_stuck' in filename

            # Añadir los datos al DataFrame
            results_df = results_df._append({
                "Algorithm": algorithm,
                "Heuristic": heuristic,
                "Explored Nodes": explored_nodes,
                "Box Stuck": 'With box_stuck' if box_stuck else 'Without box_stuck'
            }, ignore_index=True)

# Crear gráficos por cada algoritmo
for algorithm in algorithms:
    algo_df = results_df[results_df["Algorithm"] == algorithm]

    fig = px.bar(
        algo_df,
        x="Heuristic",
        y="Explored Nodes",
        color="Box Stuck",
        barmode='group',
        text_auto=True,
        title=f"Explored Nodes by Informed Algorithms per Heuristic using box_stuck in {algorithm} - Level {map_name}",
        labels={"Heuristic": "Heuristic", "Explored Nodes": "Explored Nodes", "Box Stuck": "Configuration"}
    )

    fig.update_layout(
        xaxis_title="Heuristic",
        yaxis_title="Explored Nodes",
        legend_title="Configuration"
    )

    fig.show()
