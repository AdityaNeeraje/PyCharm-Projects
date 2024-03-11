import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas
from datetime import datetime

title_color = "darkred"

with open("monthly_in_situ_co2_mlo.csv", "r") as file:
    for line_number, line in enumerate(file, 1):
        if "Yr" in line:
            line_to_skip = line_number - 1
keeling_curve_data = pandas.read_csv("monthly_in_situ_co2_mlo.csv", skiprows=line_to_skip).dropna(axis=0, ignore_index=True)
keeling_curve_data.columns = [title.strip() for title in keeling_curve_data.columns]
keeling_curve_data.drop(index=[index for index in keeling_curve_data.index.tolist() if keeling_curve_data['CO2'].iloc[:,1].loc[index].strip() == "-99.99"], inplace=True)
keeling_curve_data['Date'] = [datetime.strptime(f"{keeling_curve_data['Yr'].loc[index].strip()}-{keeling_curve_data['Mn'].loc[index].strip()}", "%Y-%m") for index in keeling_curve_data.index.tolist()]
keeling_curve_data['CO2'] = [float(value.strip()) for value in keeling_curve_data['CO2'].iloc[:,1]]
keeling_curve_data = keeling_curve_data.loc[:, ~keeling_curve_data.columns.duplicated()]
keeling_curve_data = keeling_curve_data[['Yr', 'Mn', 'Date', 'CO2']]

fontdict = {
    'color': 'darkred',
    'size': 16,
    'family': 'serif',
    "fontweight": "bold",
}
plt.figure(figsize=(16, 10))
plt.title(label="CO2 Emissions Over Time", fontdict=fontdict, pad=10)
plt.xlabel('CO2 Levels', fontdict=fontdict, labelpad=10)
plt.ylabel('Years', fontdict=fontdict, labelpad=10)
axis1 = plt.gca()
axis1.xaxis.set_major_locator(mdates.YearLocator(base=10))
axis1.xaxis.set_minor_locator(mdates.YearLocator())
axis1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.ylim(keeling_curve_data['CO2'].min()-2, keeling_curve_data['CO2'].max()+2)
plt.xlim(keeling_curve_data['Date'].min(), keeling_curve_data['Date'].max())
plt.xticks(rotation=45)
line = plt.plot(keeling_curve_data['Date'], keeling_curve_data['CO2'], label="CO2 Emissions over Time")[0]
x_data = line.get_xdata()
for n in range(len(x_data.tolist())):
    try:
        if pandas.to_datetime(x_data.tolist())[n].month in [6, 7, 8, 9, 10, 11]:
            axis1.axvspan(x_data[n], x_data[n+1], facecolor='lightgrey')
    except IndexError:
        pass
keeling_curve_data = keeling_curve_data.groupby(by='Yr').agg({'CO2': "mean"})
keeling_curve_data.index = pandas.to_datetime([datetime.strptime(year, "%Y").strftime("%Y-07-02") for year in keeling_curve_data.index])
plt.plot(keeling_curve_data.index, keeling_curve_data['CO2'], label="Yearly Average", color="green")
plt.show()