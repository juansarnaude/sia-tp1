import pandas as pd
import json
import plotly.graph_objects as go

algorithms = ['local_greedy', 'global_greedy', 'a_star']
heuristics = ['euclidean', 'manhattan', 'boxes_in_goals', 'euclidean_non_admissible', 'manhattan_non_admissible']

# Create an empty DataFrame with algorithms as rows and heuristics as columns
df = pd.DataFrame(
    data=0,
    index=algorithms,
    columns=heuristics
)

with open("configs/config_dataset.json", 'r') as file:
    config = json.load(file)
    heuristics = config["heuristics"]
    algorithms = config["algorithms"]
    map_name = config["map"].split('/')[-1].split('.')[0]  # Extraer el nombre del nivel dinámicamente


# Populate the DataFrame with values from the JSON files
for i, algorithm in enumerate(algorithms):
    for j, heuristic in enumerate(heuristics):
        with open(f"results/informedVsHeuristics/{map_name}.txt-{i}{j}.json") as file:
            data = json.load(file)
            df.iloc[i, j] = data['solution_length'][0]
        

fig = go.Figure(data=go.Heatmap(
    z=df.values,  # The values to color the cells
    x=df.columns,  # Labels for the x-axis
    y=df.index,  # Labels for the y-axis
    text=df.values,
    texttemplate="%{text}",
    textfont={"size":20},
    colorscale='Viridis',  # Choose a colorscale; 'Viridis' is one option
    colorbar=dict(title='Solution length')  # Colorbar to indicate the scale of values
))


fig.update_layout(
    title='Number of Steps for Solving Sokoban Game',
    xaxis_title='Heuristics',
    yaxis_title='Algorithms'
)

fig.show()