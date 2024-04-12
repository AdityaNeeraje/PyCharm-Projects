import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

nobel_prize_data = pd.read_csv("nobel_prize_data.csv")

# title_font = {
#     "family": "Serif",
#     "size": 16,
#     "color": "brown",
# }
# countries_with_most_awards = nobel_prize_data.groupby(by="birth_country_current").agg({"prize": "count"}).sort_values("prize", ascending=False).iloc[:12]
# countrywise_data = nobel_prize_data[nobel_prize_data["birth_country_current"].isin(list(countries_with_most_awards.index))]
# countrywise_data = countrywise_data.groupby(by=["birth_country_current", "year"]).agg({"prize": "count"}).astype(int).reset_index()
# countrywise_data = countrywise_data.pivot(index="birth_country_current", columns="year", values="prize")
# countrywise_data = countrywise_data.fillna(0).cumsum(axis=1).fillna(method="backfill").astype(int).transpose().reset_index()
# fig = px.line(data_frame=countrywise_data, x='year', y=list(countries_with_most_awards.index), title="Number of Nobel Prizes per country over time", labels=dict(birth_country_current="Country", year="Year", prize="Number of Prizes"))
# fig.update_layout(title_text="Number of Nobel Prizes per country over time", title_font=title_font, yaxis=dict(title_font=title_font), xaxis={"title_font": title_font})
# fig.show()
#
# organization_wise_data = nobel_prize_data.groupby("organization_name").agg({"prize": "count"}).sort_values("prize", ascending=True).iloc[-12:].reset_index()
# fig = px.bar(organization_wise_data, orientation='h', x='prize', y='organization_name', title="Number of Nobel Prizes per organization", color='prize', color_continuous_scale=px.colors.sequential.haline, hover_name="organization_name", hover_data='prize', labels={'prize': 'Number of Prizes', 'organization_name': 'Organization'})
# fig.show()

# city_wise_data = nobel_prize_data.groupby(by=["organization_city", "organization_name"]).agg({"prize": "count"}).reset_index()
# cities_with_most_prizes = city_wise_data.groupby(by='organization_city').agg({"prize": "sum"}).sort_values('prize', ascending=False)
# cities_with_most_prizes = cities_with_most_prizes[cities_with_most_prizes > cities_with_most_prizes['prize'].quantile(0.95)].dropna(axis=0)
# fig = px.sunburst(city_wise_data[city_wise_data['organization_city'].isin(list(cities_with_most_prizes.index))], path=['organization_city', 'organization_name'], values='prize', hover_name='organization_city', hover_data=['organization_name', 'prize'], labels={"organization_city": "City", "organization_name": "Organization", "prize": "Number of Prizes"})
# # fig.update_traces(textposition='inside')
# fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
# fig.show()

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

# plt.figure(figsize=(16, 10))
# scatter = sns.histplot(data=nobel_prize_data, x="year", hue="laureate_age", bins=20)
# plt.show()
