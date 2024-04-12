# import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime

monthly_data = pd.read_csv("monthly_deaths.csv")
monthly_data.fillna(0, inplace=True)
monthly_data["date"] = pd.to_datetime(monthly_data["date"])
monthly_data["month"] = monthly_data["date"].dt.strftime("%-m")
monthly_data = monthly_data.groupby("month").agg({"births": "mean", "deaths": "mean"})
monthly_data["month"] = [datetime.strptime(str(i), "%m").strftime("%B") for i in range(1, 13)]
monthly_data["percentage"] = monthly_data["deaths"]/monthly_data["births"]*100
# monthly_data.reset_index(inplace=True)
print(monthly_data)

plt.figure(figsize=(10,12))
# fig, ax = plt.subplots()
plt.xticks(rotation=45)
plt.plot("month","births", data=monthly_data, label="Births")
plt.plot("month", "deaths", data=monthly_data, label="Deaths")
plt.title("Average Births vs Deaths from 1841 to 1849")
plt.legend()
plt.show()