import pandas
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# # The following line of code only needs to be run during the first iteration
# import wget
# url = "https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/ml-basics/daily-bike-share.csv"
# wget.download(url)

dataframe = pandas.read_csv('daily-bike-share.csv')
dataframe['rentals'] = dataframe['rentals'].rolling(window=3).mean()
dataframe.dropna(axis=0, inplace=True, ignore_index=True)
print(dataframe.head())

# font = {
#     "font": "Serif",
#     "color": "darkred",
#     "size": 16,
#     "weight": "bold"
# }
# dataframe['dteday'] = pandas.to_datetime(dataframe['dteday'])
# plt.figure(figsize=(16, 10))
# ax = plt.subplot()
# ax.hist(dataframe['rentals'], bins=100)
# ax.set_ylabel('Frequency')
# ax.axvline(dataframe['rentals'].mean(), color='magenta', linestyle='dashed', linewidth=2)
# ax.axvline(dataframe['rentals'].median(), color='cyan', linestyle='dashed', linewidth=2)
# # ax[1].boxplot(dataframe['rentals'], vert=False)
# # ax[1].set_xlabel('Rentals')
# plt.title("Number of Cycles bought on different days of the year", fontdict=font)
# plt.show()
#
# numeric_features = ['temp', 'atemp', 'hum', 'windspeed']
# numeric_features_dict = {'temp': 'Temperature', 'atemp': 'Apparent Temperature', 'hum': 'Humidity', 'windspeed': 'Windspeed'}
# for col in numeric_features:
#     fig = plt.figure(figsize=(16, 10))
#     ax = fig.gca()
#     feature = dataframe[col]
#     feature.hist(bins=100, ax=ax)
#     ax.axvline(feature.mean(), color='magenta', linestyle='dashed', linewidth=2)
#     ax.axvline(feature.median(), color='cyan', linestyle='dashed', linewidth=2)
#     ax.set_xlabel(f"Normalized {numeric_features_dict[col]}", fontdict=font)
#     ax.set_ylabel("Frequency", fontdict=font)
#     ax.set_title(numeric_features_dict[col], fontdict=font)
# plt.show()

X, y = dataframe[['season','mnth', 'holiday','weekday','workingday','weathersit','temp', 'atemp', 'hum', 'windspeed']].values, dataframe['rentals'].values
print('Features:',X[:10], '\nLabels:', y[:10], sep='\n')
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

print('Training Set: %d rows\nTest Set: %d rows' % (X_train.shape[0], X_test.shape[0]))
from sklearn.linear_model import LinearRegression

# Fit a linear regression model on the training set
model = LinearRegression().fit(X_train, y_train)
print(model)
import numpy as np

predictions = model.predict(X_test)
np.set_printoptions(suppress=True)
print('Predicted labels: ', np.round(predictions)[:10])
print('Actual labels   : ' ,y_test[:10])
# plt.title("Number of Cycles bought on different days of the year", fontdict=font)
# plt.xlim(dataframe['dteday'].min(), dataframe['dteday'].max())
# plt.ylim(dataframe['rentals'].min(), dataframe['rentals'].max()+100)
# plt.xticks(rotation=45)
# axis1 = plt.gca()
# axis1.xaxis.set_major_locator(mdates.MonthLocator())
# plt.xlabel("Time", fontdict=font)
# plt.ylabel("Number of Cycles", fontdict=font)
# plt.plot(dataframe['dteday'], dataframe['rentals'], label='Number of Cycles')
# plt.legend(loc="upper left")
# plt.show()