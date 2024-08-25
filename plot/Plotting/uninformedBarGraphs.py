import pandas as pd
import json
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

from sokoban import sokoban

with open("configs/config_dataset_uninformed.json", 'r') as file:
    config = json.load(file)
    algorithms = config["algorithms"]
    map = config["map"]
    iteration_count = config["iteration_count"]
    execution_time = []
    mean_execution_time = []
    std_execution_time = []
    every_solution_length = []

    for i,algorithm in enumerate(algorithms):
        with open(f"results/uninformed/{map.split('/')[1]}-{i}.json", 'r') as data:
            data = json.load(data)
            execution_time = data["execution_time"]
            solution_length = data["solution_length"]
            mean_execution_time.append(np.mean(execution_time))
            std_execution_time.append(np.std(execution_time))
            every_solution_length.append(solution_length[0])

    df1 = pd.DataFrame({
        "Algorithm": algorithms,
        "Execution Time": mean_execution_time,
    })
    fig1 = px.bar(df1, x="Algorithm", y="Execution Time", color="Algorithm", title=f"Tiempos de ejecución - Nivel {map.split('/')[1].split('.')[0]}" ,error_y=std_execution_time)
    fig1.show()

    df2 = pd.DataFrame({
        "Algorithm": algorithms,
        "Number of Steps": every_solution_length,
    })
    fig2 = px.bar(df2, x="Algorithm", y="Number of Steps", color="Algorithm", title=f"Cantidad de Pasos - Nivel {map.split('/')[1].split('.')[0]}")
    fig2.show()


