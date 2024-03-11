import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import seaborn as sns

fontdict = {
    'family': 'serif',
    'weight': 'bold',
    'size': 22
}
# formatter = DateFormatter()

monthly_data = pd.read_csv("monthly_deaths.csv")
monthly_data["pct_deaths"] = monthly_data["deaths"] / monthly_data["births"] * 100
monthly_data["date"] = pd.to_datetime(monthly_data["date"])
monthly_data["category"] = ((monthly_data["date"].dt.year < 1847) | (
        (monthly_data["date"].dt.year == 1847) & (monthly_data["date"].dt.month < 6)))

# # Before and After comparison
# plt.figure(figsize=(10, 12))
# plt.grid(which="major", color='gray', linestyle='--', alpha=0.5)
# axis1 = plt.subplot()
# axis1.set_xlim(monthly_data["date"][0], monthly_data["date"][len(monthly_data["date"]) - 1])
# axis1.set_xlabel("Date", fontdict=fontdict)
# axis1.xaxis.set_major_locator(mdates.YearLocator())
# axis1.xaxis.set_minor_locator(mdates.MonthLocator())
# axis1.set_ylabel('Percentage of Deaths vs Births', fontdict=fontdict, color='red')
# axis1.plot("date", "pct_deaths", "g--", data=monthly_data[monthly_data["category"] == True],
#            label='Before Washing Hands')
# axis1.plot("date", "pct_deaths", "ch-", data=monthly_data[monthly_data["category"] == False],
#            label='After Washing Hands')
# axis1.set_ylim(monthly_data["pct_deaths"].min(), monthly_data["pct_deaths"].max() * 1.05)
# print("Average percentage of deaths before washing hands was introduced =",
#       '%.2f' % (monthly_data["pct_deaths"][monthly_data["category"] == True].mean()), "%")
# print("Average percentage of deaths after washing hands was introduced =", '%.2f' % (monthly_data["pct_deaths"][monthly_data["category"] == False].mean()), "%")
# yticks = np.append(axis1.get_yticks(), [monthly_data["pct_deaths"].max()])
# monthly_data["pct_deaths"] = monthly_data["pct_deaths"].rolling(6, closed='right').mean()
# axis1.plot("date", "pct_deaths", "r-", data=monthly_data, lw=2, label='6-month Rolling Average')
# axis1.set_yticks(yticks)
# axis1.legend()
# plt.show()

# Testing for Statistical Significance
plt.figure(figsize=(12,10), facecolor="olivegreen")
sns.set_style(rc = {'axes.facecolor': 'lightsteelblue'})
axis1 = sns.boxplot(x='category', y='pct_deaths', data=monthly_data, order=[True, False], color='cyan')
axis1.set_title("Variation in Percentage of Deaths Before and After Washing Hands")
axis1.set_xticklabels(["Before", "After"])
axis1.set_ylabel("Number of Deaths per 100 Births", fontdict=fontdict, color="cyan")
axis1.set_xlabel("")
plt.show()

# plt.figure(figsize=(10, 12))
# axis1 = plt.subplot()
# monthly_data["date"] = pd.to_datetime(monthly_data["date"])
# axis1.set_xlabel('Date', fontdict=fontdict)
# axis1.xaxis.set_major_locator(mdates.YearLocator())
# axis1.xaxis.set_minor_locator(mdates.MonthLocator())
# axis1.set_ylabel('Births', fontdict=fontdict, color='blue')
# axis1.plot("date", "births", "b-", data=monthly_data, label="Births")
# # axis1.yaxis.title("Births")
# # axis1.set_xlim(monthly_data["date"].min, monthly_data["date"].max)
# axis2 = axis1.twinx()
# axis2.set_ylabel('Deaths', fontdict=fontdict, color='darkred')
# axis2.plot("date", "deaths", "r-", data=monthly_data, label="Deaths")
# # axis2.yaxis.title("Deaths")
# plt.legend()
# plt.show()
