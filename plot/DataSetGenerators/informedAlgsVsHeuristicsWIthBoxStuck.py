import json

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
            sokoban(algorithm, [heuristic], map, f"results/informedVsHeuristicsBoxStuck/{map.split('/')[1]}-{i}{j}.json",iteration_count)
            sokoban(algorithm, [heuristic,"box_stuck"], map, f"results/informedVsHeuristicsBoxStuck/{map.split('/')[1]}-{i}{j}box_stuck.json",iteration_count)