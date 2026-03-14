import pandas as pd

print("Loading datasets...")

artists = pd.read_csv("../data/artist_info.csv")
charts = pd.read_csv("../data/chart_positions.csv")

artists.columns = artists.columns.str.lower().str.strip()
charts.columns = charts.columns.str.lower().str.strip()

artists['artist'] = artists['artist'].str.lower().str.strip()
charts['artist'] = charts['artist'].str.lower().str.strip()

charts['date'] = pd.to_datetime(charts['date'])

charts['weeks-on-board'] = charts['weeks-on-board'].fillna(
    charts['weeks-on-board'].median()
)

charts['last-week'] = charts['last-week'].fillna(0)

data = charts.merge(artists,on="artist",how="left")

data.to_csv("../data/cleaned_data.csv",index=False)

print("Data cleaned and saved.")
