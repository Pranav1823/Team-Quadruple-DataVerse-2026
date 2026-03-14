import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("../data/cleaned_data.csv")

data['hit'] = data['peak-rank'].apply(lambda x: 1 if x <= 10 else 0)

features = data[['weeks-on-board','last-week']]
target = data['hit']

X_train,X_test,y_train,y_test = train_test_split(
    features,target,test_size=0.2,random_state=42
)

model = RandomForestClassifier(n_estimators=50)

model.fit(X_train,y_train)

importance = model.feature_importances_

plt.figure(figsize=(8,5))

sns.barplot(
    x=importance,
    y=features.columns,
    palette="magma"
)

plt.title("Factors Influencing Hit Songs")

plt.show()

print("Insight:")
print("Weeks on chart strongly influences hit song prediction.")
