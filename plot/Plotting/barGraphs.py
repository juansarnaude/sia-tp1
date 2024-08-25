import pandas as pd
import json
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

from sokoban import sokoban

with open("configs/config_dataset.json", 'r') as file:
    config = json.load(file)
    algorithms = config["algorithms"]
    heuristics = config["heuristics"]
    map = config["map"]
    iteration_count = config["iteration_count"]
    execution_time = []
    mean_execution_time = []
    std_execution_time = []

    for i,algorithm in enumerate(algorithms):
        for j,heuristic in enumerate(heuristics):
            with open(f"results/informedVsHeuristics/{map.split('/')[1]}-{i}{j}.json", 'r') as data:
                data = json.load(data)
                execution_time = data["execution_time"]
                mean_execution_time.append(np.mean(execution_time))
                std_execution_time.append(np.std(execution_time))
        df = pd.DataFrame({
            "Heuristic": heuristics,
            "Execution Time": mean_execution_time,
        })
        fig = px.bar(df, x="Heuristic", y="Execution Time", color="Heuristic", title=algorithms[i],error_y=std_execution_time)
        fig.show()
        mean_execution_time.clear()
        std_execution_time.clear()


