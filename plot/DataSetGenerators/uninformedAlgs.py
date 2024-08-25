import pandas as pd
import json
import plotly.graph_objects as go

from sokoban import sokoban

with open("configs/config_dataset_uninformed.json", 'r') as file:
    config = json.load(file)
    algorithms = config["algorithms"]
    map = config["map"]
    iteration_count = config["iteration_count"]
    heuristics = []

    # # Generate data set
    for i, algorithm in enumerate(algorithms):
        sokoban(algorithm,heuristics, map, f"results/uninformed/{map.split('/')[1]}-{i}.json", iteration_count)