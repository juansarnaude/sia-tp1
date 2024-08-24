import pandas as pd
import json
import plotly.graph_objects as go

algorithms = ['local_greedy', 'global_greedy', 'a_star']
heuristics = ['euclidean', 'manhattan', 'boxes_in_goals', 'euclidean_non_admissible', 'manhattan_non_admissible']

# # Generate data set
# for i, algorithm in enumerate(algorithms):
#     for j, heuristic in enumerate(heuristics):
#         sokoban(algorithm, [heuristic], 'maps/lv1.txt', f"results/informedVsHeuristics/r{i}{j}.json")

# Create an empty DataFrame with algorithms as rows and heuristics as columns
df = pd.DataFrame(
    data=0,
    index=algorithms,
    columns=heuristics
)

# Populate the DataFrame with values from the JSON files
for i, algorithm in enumerate(algorithms):
    for j, heuristic in enumerate(heuristics):
        with open(f"results/informedVsHeuristics/r{i}{j}.json") as file:
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
    xaxis_title='Algorithms',
    yaxis_title='Heuristics'
)

fig.show()