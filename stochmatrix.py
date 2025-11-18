import pandas as pd
import numpy as np

df = pd.read_csv("filtered_tennis_data.csv")
all_players = pd.concat([df["Player_1"], df["Player_2"]])
total_unique_players = all_players.nunique()
print(total_unique_players)
