# This code displays two bar charts - the first depicting the top 12 countries, with awards ordered in the order of
# which field a country has most awards in. In the second graph, the awards are ordered in alphabetical order of the
# fields.

import pandas as pd
import plotly.io as pio
import plotly.express as px

nobel_prize_data = pd.read_csv("nobel_prize_data.csv")

title_font = {
    "family": "Serif",
    "size": 16,
    "color": "brown",
}
pio.templates.default = "plotly_dark"
countrywise_data = nobel_prize_data.groupby(by="birth_country_current").agg({"prize": "count"}).sort_values("prize", ascending=False).iloc[:12]
category_wise_data = nobel_prize_data.groupby(by=["birth_country_current", "category"]).agg({"prize": "count"}).reset_index()
category_wise_data = category_wise_data[category_wise_data["birth_country_current"].isin(list(countrywise_data.index))]
category_wise_data["total_number"] = [countrywise_data.loc[country, "prize"] for country in category_wise_data["birth_country_current"].tolist()]
category_wise_data.sort_values(by=["total_number", "prize"], ascending=[True, True], inplace=True)
fig = px.bar(category_wise_data, y='birth_country_current', x='prize', orientation='h', hover_data=["birth_country_current", "total_number", "category", "prize"], height=400, labels={"birth_country_current": "Country", "total_number": "Total Number", "category": "Category", "prize": "Number of Prizes"}, color="prize", color_continuous_scale=px.colors.sequential.Oranges)
fig.update_layout(title_text="Number of Nobel Prizes by Country", title_font=title_font, yaxis=dict(title="Country", title_font=title_font), xaxis=dict(title="Number of Prizes", title_font=title_font))
fig.show()


title_font = {
    "family": "Serif",
    "size": 16,
    "color": "brown",
}
pio.templates.default = "plotly_dark"
number_of_countries = 12
countrywise_data = nobel_prize_data.groupby(by="birth_country_current").agg({"prize": "count"}).sort_values("prize", ascending=False).iloc[:number_of_countries]
category_wise_data = nobel_prize_data.groupby(by=["birth_country_current", "category"]).agg({"prize": "count"}).reset_index()
category_wise_data = category_wise_data[category_wise_data["birth_country_current"].isin(list(countrywise_data.index))]
category_wise_data["total_number"] = [countrywise_data.loc[country, "prize"] for country in category_wise_data["birth_country_current"].tolist()]
category_wise_data.sort_values(by=["total_number", "birth_country_current", "category"], inplace=True)
fig = px.bar(category_wise_data, y='birth_country_current', x='prize', orientation='h', hover_data=["birth_country_current", "total_number", "category", "prize"], height=400, labels={"birth_country_current": "Country", "total_number": "Total Number", "category": "Category", "prize": "Number of Prizes"}, color="category")
fig.update_yaxes(nticks=number_of_countries)
fig.update_layout(title_text="Number of Nobel Prizes by Country", title_font=title_font, yaxis=dict(title="Country", title_font=title_font), xaxis=dict(title="Number of Prizes", title_font=title_font))
fig.show()
