import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression

def delimit(string):
    if len(str(string).split(".")) == 1:
        try:
            int(string)
        except ValueError:
            return None
        string = str(string).rjust(3 * ((len(str(string))-1) // 3 + 1), " ")
        return ",".join([string[i:i + 3] for i in range(0, len(string), 3)]).strip()
    else:
        try:
            float(str(string))
        except ValueError:
            return None
        significant = str(string).split(".")[0]
        significant = significant.rjust(3 * ((len(significant)-1) // 3 + 1), " ")
        return ",".join([significant[i:i + 3] for i in range(0, len(significant), 3)]).strip() + "." + str(string).split(".")[1]


dataframe = pd.read_csv('unprocessed_data.csv')
dataframe.drop_duplicates(subset='Movie_Title', inplace=True, ignore_index=True)

for column in ['USD_Production_Budget', 'USD_Worldwide_Gross', 'USD_Domestic_Gross']:
    dataframe[column] = [int(element.strip().replace("$", "").replace(",", "")) for element in dataframe[column]]
#     Alternatively, a better method would have been dataframe[column] = dataframe[column].astype(str).str.replace(",", "").str.replace("$","")
dataframe['Release_Date'] = pd.to_datetime(dataframe['Release_Date'])

# films_with_zero_revenue = dataframe[dataframe['USD_Worldwide_Gross'] == 0]
# print(f"The number of films with zero gross worldwide revenue is: {films_with_zero_revenue.shape[0]}")
#
# print(
#     f"The average worlwide gross for movies released after 1960 is: {delimit(round(dataframe['USD_Worldwide_Gross'][dataframe['USD_Worldwide_Gross'] != 0][dataframe['Release_Date'].dt.year > 1960].mean(), 2))}")
# revenue_gain = dataframe['USD_Worldwide_Gross'] - dataframe['USD_Production_Budget']
# print(
#     f"The maximum revenue generated by a single film is: ${delimit(revenue_gain.max())} for the movie {dataframe['Movie_Title'].iloc[revenue_gain.idxmax()]}")
# print(
#     f"The maximum amount lost by a single film is: {delimit(- revenue_gain.min())} for the movie {dataframe['Movie_Title'].iloc[revenue_gain.idxmin()]}")
#
# print(
#     f"The average revenue gained/lost by the movies in the last quantile is: {delimit(revenue_gain[revenue_gain < revenue_gain.quantile(0.25)].mean())}")
# print(
#     f"The maximum revenue of a movie in the last quantile is {delimit(revenue_gain[revenue_gain < revenue_gain.quantile(0.25)].max())}")
#
# plt.figure(figsize=(8, 6))
# with sns.axes_style('darkgrid'):
#     ax = sns.scatterplot(data=dataframe, x='USD_Production_Budget', y='USD_Worldwide_Gross', hue="USD_Worldwide_Gross", size="USD_Worldwide_Gross")
#     ax.set(ylim=(0, 3000000000),
#            xlim=(0, 450000000),
#            ylabel='Revenue in $ billions',
#            xlabel='Budget in $100 millions')
#     plt.show()

# plt.figure(figsize=(12, 9))
# with sns.axes_style('ticks'):
#     ax = sns.scatterplot(data=dataframe, x='Release_Date', y='USD_Production_Budget', hue="USD_Worldwide_Gross", size="USD_Worldwide_Gross")
#     ax.set(ylim=(0, dataframe['USD_Production_Budget'].max()), xlim=(dataframe['Release_Date'].min(), dataframe['Release_Date'].max()), ylabel="Budget in 100 Million USD", xlabel='Release Date')
#     ax.xaxis.set_major_locator(mdates.YearLocator(base=10))
#     plt.show()

old_movies = dataframe[dataframe['Release_Date'].dt.year < 1970]
new_movies = dataframe[dataframe['Release_Date'].dt.year >= 1970]
regression = LinearRegression()

# Explanatory variables or features
X_1 = pd.DataFrame(old_movies, columns=['USD_Production_Budget'])
X_2 = pd.DataFrame(new_movies, columns=['USD_Production_Budget'])

# Response variable or target
y_1 = pd.DataFrame(old_movies, columns=['USD_Worldwide_Gross'])
y_2 = pd.DataFrame(new_movies, columns=['USD_Worldwide_Gross'])

regression.fit(X_1, y_1)
print(f"For movies released prior to 1970, the intercept of the linear regression function is {round(regression.intercept_[0], 2)} and the slope is {round(regression.coef_[0][0], 2)}")
print(f"For movies released prior to 1970, the R^2 metric of the linear regression function is {round(100*regression.score(X_1, y_1), 2)}%")
print("\n")

regression.fit(X_2, y_2)
print(f"For movies released after 1970, the intercept of the linear regression function is {round(regression.intercept_[0], 2)} and the slope is {round(regression.coef_[0][0], 2)}")
print(f"For movies released after 1970, the R^2 metric of the linear regression function is {round(100*regression.score(X_2, y_2), 2)}%")
# plt.figure(figsize=(12, 10))
# with sns.axes_style("dark"):
#     plt.xlim(0, old_movies['USD_Production_Budget'].max()*1.01)
#     plt.ylim(0, old_movies['USD_Worldwide_Gross'].max()*1.01)
#     sns.regplot(data=old_movies, x='USD_Production_Budget', y='USD_Worldwide_Gross', scatter_kws={"alpha": 0.4, "color": "#2f4b7c"}, line_kws={"color": "#ff7c43", "lw": 5})
#     plt.show()
#
# plt.figure(figsize=(12, 10))
# with sns.axes_style("dark"):
#     plt.xlim(new_movies['USD_Production_Budget'].min()*0.99, new_movies['USD_Production_Budget'].max()*1.01)
#     plt.ylim(new_movies['USD_Worldwide_Gross'].min()*0.99, new_movies['USD_Worldwide_Gross'].max()*1.01)
#     sns.regplot(data=new_movies, x='USD_Production_Budget', y='USD_Worldwide_Gross', scatter_kws={"alpha": 0.4, "color": "#2f4b7c"}, line_kws={"color": "#ff7c43", "lw": 5})
#     plt.show()