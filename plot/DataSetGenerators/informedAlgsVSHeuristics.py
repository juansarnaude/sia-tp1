import pandas as pd
import json
import plotly.graph_objects as go

from sokoban import sokoban

with open("configs/config_dataset.json", 'r') as file:
    config = json.load(file)
    algorithms = config["algorithms"]
    heuristics = config["heuristics"]
    map = config["map"]
    iteration_count = config["iteration_count"]
    
    # # Generate data set
    for i, algorithm in enumerate(algorithms):
        for j, heuristic in enumerate(heuristics):
            sokoban(algorithm, [heuristic], map, f"results/informedVsHeuristics/{map.split('/')}-{i}{j}.json", iteration_count)