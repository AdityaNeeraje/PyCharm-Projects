# This code displays a chloropleth map of different countries and the number of prizes they have won.

import pandas as pd
import plotly.io as pio
import plotly.express as px
import pycountry

nobel_prize_data = pd.read_csv("nobel_prize_data.csv")

pio.templates.default = "seaborn"
category_wise_data = nobel_prize_data.groupby(by=['birth_country_current', 'category'])['prize'].count().reset_index()
countrywise_data = category_wise_data.groupby(by="birth_country_current").agg({"prize": "sum"}).sort_values("prize", ascending=False)
ISO_codes_list = []
for country in list(countrywise_data.index):
    try:
        ISO_codes_list.append(pycountry.countries.search_fuzzy(country)[0].alpha_3)
    except LookupError:
        countrywise_data.drop(index=country, axis=0, inplace=True)
countrywise_data["ISO_codes"] = ISO_codes_list
fig = px.choropleth(countrywise_data, locations="ISO_codes", color="prize", hover_name=list(countrywise_data.index), color_continuous_scale=px.colors.sequential.Plasma)
fig.show()
