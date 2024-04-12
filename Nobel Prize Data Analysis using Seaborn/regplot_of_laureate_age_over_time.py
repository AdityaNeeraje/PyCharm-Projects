import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

nobel_prize_data = pd.read_csv("nobel_prize_data.csv")

nobel_prize_data['year'] = pd.to_datetime(pd.to_datetime(nobel_prize_data['year'], format="%Y").dt.strftime("10-12-%Y"))
nobel_prize_data.dropna(axis=0, subset='birth_date', ignore_index=True, inplace=True)
nobel_prize_data['laureate_age'] = (nobel_prize_data['year'] - pd.to_datetime(nobel_prize_data['birth_date'])).dt.days
nobel_prize_data = nobel_prize_data.groupby(by='year').agg({"laureate_age": "mean"}).reset_index()
nobel_prize_data['laureate_age'] = nobel_prize_data['laureate_age'] // 365
nobel_prize_data['laureate_age'] = nobel_prize_data['laureate_age'].rolling(window=6).mean()
nobel_prize_data['year'] = nobel_prize_data['year'].dt.strftime("%Y").astype(int)
nobel_prize_data.dropna(inplace=True)
X = pd.DataFrame(nobel_prize_data['year'])
y = pd.DataFrame(nobel_prize_data['laureate_age']).astype(float)
plt.figure(figsize=(16, 10))
scatter = sns.regplot(x=X, y=y, scatter_kws={"color": "purple", "alpha": 0.5}, line_kws={"color": "orange"})
scatter.set_title(label="Average age of laureates over time", fontdict={"weight": "bold", "size": 16, "color": "darkred"})
scatter.set_xlabel("Year", fontdict={"weight": "bold", "size": 14, "color": "blue"})
scatter.set_ylabel("Laureate Age", fontdict={"weight": "bold", "size": 14, "color": "purple"})
scatter.set_xlim(nobel_prize_data['year'].min()*0.9999, nobel_prize_data['year'].max()*1.0001)
plt.show()
