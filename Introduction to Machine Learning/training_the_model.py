import pandas
import wget
import statsmodels.formula.api as smf
import graphing
import joblib
# We need to install plotly for graphing.py to work, because it utilizes plotly.express as px. Again, this is only for the first time


# wget allows us to download data from the web. We need to run the next two lines of code only during the first time running the code.
# data_url = "https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/doggy-boot-harness.csv"
# wget.download(url=data_url)
# graphing_url = "https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/graphing.py"
# wget.download(url=graphing_url)

df = pandas.read_csv("doggy-boot-harness.csv")

formula = "boot_size ~ harness_size"
# The next line of code creates a model but does not train it.
model = smf.ols(formula=formula, data=df)
if not hasattr(model, 'params'):
    print("Model selected but it does not have parameters set. It needs to be trained.")

# THe next few lines of code help train the machine learning model.
fitted_model = model.fit()
print(f"The following model parameters have been found:\nLine slope: {fitted_model.params[1]}\nLine intercept: {fitted_model.params[0]}")
graphing.scatter_2D(df, label_x="harness_size", label_y="boot_size", trendline=lambda x: fitted_model.params[1]*x + fitted_model.params[0], show=True)

# THe following lines of code submit a harness_size and get the machine learning model to estimate a boot_size.
# boot_size is a dataframe whose 1st index we can acquire by using [0]
harness_size = 53.5
boot_size = fitted_model.predict({"harness_size": [harness_size]})[0]
print(f"Approximate boot size for a harness size of {harness_size}: {boot_size}")

# The following lines of code save the model to a particular file
filename = "./machine_learning_model.pkl"
joblib.dump(fitted_model,filename)
print("Model saved")
