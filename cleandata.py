import pandas as pd

df = pd.read_csv("atp_tennis.csv")
columns_to_keep = ["Date", "Player_1", "Player_2", "Winner"]
df["Date"] = pd.to_datetime(df["Date"])
df_date_filtered = df[df["Date"] >= "2015-01-01"].copy()
df_final_filtered = df_date_filtered[columns_to_keep]
output_filename = "filtered_tennis_data.csv"
df_final_filtered.to_csv(output_filename, index=False)
