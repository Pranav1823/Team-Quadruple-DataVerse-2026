import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("../data/cleaned_data.csv")

plt.figure(figsize=(12,6))

sns.histplot(
    data['weeks-on-board'],
    bins=40,
    kde=True,
    color="purple"
)

plt.title("Song Longevity Distribution")
plt.xlabel("Weeks on Chart")

plt.show()

print("Insight:")
print("Most songs remain on the chart for a short time while only a few stay long.")
