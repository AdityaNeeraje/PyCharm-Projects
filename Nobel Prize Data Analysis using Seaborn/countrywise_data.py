import pandas as pd
import plotly.express as px

nobel_prize_data = pd.read_csv("nobel_prize_data.csv")

countrywise_data = nobel_prize_data.groupby(by='birth_country_current').agg({"category": "count"})
countries_with_many_awards = countrywise_data[countrywise_data['category'] > 10]
fig = px.pie(countries_with_many_awards, values='category', names=countries_with_many_awards.index, title="Nobel Prizes by country", hover_data=['category'], labels={'category': "Number of Awards", "birth_country_current": "Country of Origin"})
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()
