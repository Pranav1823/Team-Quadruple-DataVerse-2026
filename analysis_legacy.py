import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("../data/cleaned_data.csv")

top_artists = data.groupby("artist")["song"].count().sort_values(ascending=False).head(15)

plt.figure(figsize=(12,7))

sns.barplot(
    x=top_artists.values,
    y=top_artists.index,
    palette="viridis"
)

plt.title("Top Artists Dominating Billboard Charts")
plt.xlabel("Number of Chart Appearances")
plt.ylabel("Artist")

plt.show()

print("Insight:")
print("These artists consistently appear on the charts, showing sustained popularity.")
