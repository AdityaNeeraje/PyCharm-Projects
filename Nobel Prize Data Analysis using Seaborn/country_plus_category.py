import pandas as pd
import plotly.express as px

nobel_prize_data = pd.read_csv("nobel_prize_data.csv")

category_wise_data = nobel_prize_data.groupby(by=['birth_country_current', 'category'])['prize'].count().reset_index()
countrywise_data = category_wise_data.groupby(by="birth_country_current").sum()["prize"]
countries_to_keep = [country for country in countrywise_data.index if countrywise_data[country] > 10]
category_wise_data = category_wise_data[category_wise_data['birth_country_current'].isin(countries_to_keep)].reset_index()

fig = px.sunburst(category_wise_data, path=['birth_country_current', 'category'], values='prize')
# fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
fig.show()
