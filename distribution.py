import pandas as pd


df = pd.read_csv("netflix_titles.csv")


print(df.shape)
print(df.columns)
df.head()

import matplotlib.pyplot as plt
import seaborn as sns


sns.countplot(data=df, x='type', palette='Set2')
plt.title('Distribution of Content Types on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()

