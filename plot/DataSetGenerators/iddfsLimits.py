import json

from sokoban import sokoban

with open("configs/config_dataset_iddfs.json", 'r') as file:
    config = json.load(file)
    map = config["map"]
    limits = config["iddfs_limits"]
    iterations=config["iteration_count"]

    # # Generate data set
    for l in limits:
            sokoban("iddfs", [], map, f"results/iddfs_limits/{map.split('/')[1]}-{l}.json",iterations,iddfs_limit=l)