import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("../data/cleaned_data.csv")

sample_data = data.sample(5000)

plt.figure(figsize=(12,6))

sns.scatterplot(
    x="peak-rank",
    y="weeks-on-board",
    data=sample_data,
    alpha=0.4,
    color="teal"
)

plt.title("Launch Rank vs Chart Longevity")

plt.show()

print("Insight:")
print("Songs peaking near rank #1 often stay longer,")
print("but slow-rising songs can also achieve longevity.")
