# This pyplot shows the rolling average of Nobel Prizes per year and the average percentage of awards each laureate won.

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

nobel_prize_data = pd.read_csv("nobel_prize_data.csv")

nobel_prize_data['birth_date'] = pd.to_datetime(nobel_prize_data['birth_date'])
first_term = pd.Series([element[0] for element in nobel_prize_data['prize_share'].str.split("/").tolist()]).astype(
    "int64")
second_term = pd.Series([element[1] for element in nobel_prize_data['prize_share'].str.split("/").tolist()]).astype(
    "int64")
nobel_prize_data['prize_percentage'] = first_term * 100 / second_term

yearwise_count = nobel_prize_data.groupby("year").agg({"prize": "count", "prize_percentage": "mean"})
yearwise_count["prize_percentage"] = yearwise_count["prize_percentage"].rolling(window=5).mean()
rolling_average = yearwise_count['prize'].rolling(window=5).mean()
rolling_average.rename("rolling_average", inplace=True)
rolling_average.dropna(axis=0, inplace=True)
rolling_average = pd.merge(left=rolling_average, right=yearwise_count, how="inner", on="year")
rolling_average.index = pd.to_datetime(rolling_average.index, format="%Y")

fontdict = {
    'color': 'darkred',
    'size': 16,
    'family': 'serif',
    "fontweight": "bold",
}

plt.figure(figsize=(16, 10))
plt.title("Number of Nobel Prizes per year", fontdict=fontdict)
axis1 = plt.gca()
axis2 = axis1.twinx()
axis2.set_ylabel("Average percentage of the prize won per laureate", fontdict=fontdict, color="brown")
axis2.plot(rolling_average.index, rolling_average["prize_percentage"], color="brown", linewidth=2)
# axis3 = axis2.twinx()
# axis3.plot(rolling_average.index, rolling_average["prize_percentage"], color="blue", linewidth=2)
# axis3.invert_yaxis()
axis1.xaxis.set_major_locator(mdates.YearLocator(base=5))
axis1.xaxis.set_minor_locator(mdates.YearLocator())
axis1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
axis1.set_xlabel("Year", fontdict=fontdict)
axis1.set_ylabel("Number of Nobel Prizes awarded in the year", fontdict=fontdict, color="purple")
plt.xlim(rolling_average.index.min(), rolling_average.index.max())
axis1.set_ylim(min(rolling_average['prize'].min(), rolling_average['rolling_average'].min())*0.99, max(rolling_average['prize'].max(), rolling_average['rolling_average'].max())*1.05)
axis1.scatter(data=rolling_average, x=rolling_average.index, y='prize', c='#2ca02c', marker="^", alpha=0.7)
axis1.plot(rolling_average.index, rolling_average['rolling_average'], 'mo--', linewidth=2)

# The following two lines of code are very usfeul. They bring the axis1 graph to the fore and axis2 graph below.
# They need to be written at the bottom. If not, the code will not work as intended. ALso, the axis1.set_frame_on(False)
# makes the axis1 canvas transparent. If not, the axis2 would not be visible.
axis1.set_zorder(axis2.get_zorder()+1)
axis1.set_frame_on(False)
plt.show()

pio.templates.default = "plotly_dark"
px.defaults.color_continuous_scale = px.colors.sequential.Blackbody
fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Scatter(x=rolling_average.index, y=rolling_average['rolling_average'], name="Number of Prizes"), secondary_y=False)
fig.add_trace(go.Scatter(x=rolling_average.index, y=rolling_average['prize_percentage'], name="Prize Percentage"), secondary_y=True)
# fig = px.scatter(rolling_average, x=rolling_average.index, y='prize', title="Number of Nobel Prizes per year")
fig.update_layout(title_text="Number of Nobel Prizes per Year",
                  title={"automargin": True, "yref": 'paper'},
                  title_font={"family": "Times New Roman", "color": "darkred", "size": 50},
                  # yaxis={"title": "Number of Prizes",
                  #        "title_font": {"family": "Times New Roman", "color": "purple", "size": 16}},
                  xaxis={"title": "Year", "title_font": {"family": "Times New Roman", "size": 16, "color": "darkred"}})
fig.update_xaxes(dtick="M60", griddash="longdashdot", linewidth=2, minor=dict(dtick="M12", showgrid=False))
fig.update_yaxes(title_text="Number of Prizes", secondary_y=False, title_font=dict(family='Serif', size=16, color="purple"))
fig.update_yaxes(title_text="Percentage of Prize received per Laureate", secondary_y=True, title_font = dict(family='Serif', size=16, color="brown"))
fig.show()
