import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("../data/cleaned_data.csv")

data['date'] = pd.to_datetime(data['date'])

data['year'] = data['date'].dt.year
data['decade'] = (data['year']//10)*10

decade_hits = data.groupby("decade")["song"].count()

plt.figure(figsize=(12,6))

sns.lineplot(
    x=decade_hits.index,
    y=decade_hits.values,
    marker="o"
)

plt.title("Evolution of Billboard Hits Across Decades")

plt.show()

print("Insight:")
print("Music trends evolve significantly across decades.")
