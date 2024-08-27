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
    every_explored_nodes_count = []

    for i,algorithm in enumerate(algorithms):
        with open(f"results/uninformed/{map.split('/')[1]}-{i}.json", 'r') as data:
            data = json.load(data)
            execution_time = data["execution_time"]
            solution_length = data["solution_length"]
            explored_nodes_count = data["explored_nodes_count"]
            mean_execution_time.append(np.mean(execution_time))
            std_execution_time.append(np.std(execution_time))
            every_solution_length.append(solution_length[0])
            every_explored_nodes_count.append(explored_nodes_count[0])

    df1 = pd.DataFrame({
        "Algorithm": algorithms,
        "Execution Time": mean_execution_time,
    })
    fig1 = px.bar(df1, x="Algorithm", y="Execution Time", color="Algorithm", title=f"Execution Time Across Uninformed Algorithms- Level {map.split('/')[1].split('.')[0]}" ,error_y=std_execution_time,text_auto=True)
    
    # Update layout for bigger font sizes
    fig1.update_layout(
        font=dict(
            size=32           # Increase this value to make the font bigger
        ),
        title=dict(
            font=dict(size=32)  # Title font size
        ),
        xaxis=dict(
            title_font=dict(size=24),  # X-axis title font size
            tickfont=dict(size=20)     # X-axis labels font size
        ),
        yaxis=dict(
            title_font=dict(size=24),  # Y-axis title font size
            tickfont=dict(size=20)     # Y-axis labels font size
        ),
        legend=dict(
            font=dict(size=20)  # Legend font size
        )
    )
    
    fig1.show()

    df2 = pd.DataFrame({
        "Algorithm": algorithms,
        "Steps to solution": every_solution_length,
    })
    fig2 = px.bar(df2, x="Algorithm", y="Steps to solution", color="Algorithm", title=f"Optimality of Solutions Across Uninformed Algorithms - Level {map.split('/')[1].split('.')[0]}",text_auto=True)
    
    # Update layout for bigger font sizes
    fig2.update_layout(
        font=dict(
            size=32           # Increase this value to make the font bigger
        ),
        title=dict(
            font=dict(size=32)  # Title font size
        ),
        xaxis=dict(
            title_font=dict(size=24),  # X-axis title font size
            tickfont=dict(size=20)     # X-axis labels font size
        ),
        yaxis=dict(
            title_font=dict(size=24),  # Y-axis title font size
            tickfont=dict(size=20)     # Y-axis labels font size
        ),
        legend=dict(
            font=dict(size=20)  # Legend font size
        )
    )

    fig2.show()

    df3 = pd.DataFrame({
        "Algorithm": algorithms,
        "Explored nodes count": every_explored_nodes_count,
    })
    fig3 = px.bar(df3, x="Algorithm", y="Explored nodes count", color="Algorithm", title=f"Explored Nodes Count Across Uninformed Algorithms - Level {map.split('/')[1].split('.')[0]}",text_auto=True)
    
    # Update layout for bigger font sizes
    fig3.update_layout(
        font=dict(
            size=32           # Increase this value to make the font bigger
        ),
        title=dict(
            font=dict(size=32)  # Title font size
        ),
        xaxis=dict(
            title_font=dict(size=24),  # X-axis title font size
            tickfont=dict(size=20)     # X-axis labels font size
        ),
        yaxis=dict(
            title_font=dict(size=24),  # Y-axis title font size
            tickfont=dict(size=20)     # Y-axis labels font size
        ),
        legend=dict(
            font=dict(size=20)  # Legend font size
        )
    )

    fig3.show()


