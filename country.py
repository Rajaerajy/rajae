import pandas as pd


df = pd.read_csv("netflix_titles.csv")


print(df.shape)
print(df.columns)
df.head()

import matplotlib.pyplot as plt


top_countries = df['country'].value_counts().head(10)
top_countries.plot(kind='barh', color='skyblue')
plt.title('Top 10 Countries with Most Netflix Titles')
plt.xlabel('Number of Titles')
plt.ylabel('Country')
plt.gca().invert_yaxis()
plt.show()

