import pandas as pd
import numpy as np
from keras.layers import Dense
from keras.models import Sequential
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

# analyze full and reduced data
data = pd.read_csv("./Data/full_data.csv")
# data = pd.read_csv("./Data/reduced_data.csv")

# response variables
r1 = data["total_deaths"]
r2 = data["total_deaths_per_million"]
r3 = data["total_cases"]
r4 = data["total_cases_per_million"]

# drop variables confounded to response variables & categorical variables
data.drop(columns=["total_deaths_per_million", "total_deaths", "iso_code", "Unnamed: 0", "continent",
            "location", "date", "tests_units"], inplace=True)
# data = data[["stringency_index", "diabetes_prevalence", "population"]]
data.fillna(0, inplace=True)

# split into training and testing data
x_train, x_test, y_train, y_test = train_test_split(data, r2, test_size=0.2, random_state=0)

# 1. neural network
# model = Sequential()
# model.add(Dense(50, activation="sigmoid", input_dim=x_train.shape[1]))
# model.add(Dense(50, activation="sigmoid"))
# model.add(Dense(10, activation="softmax"))

# print(model.summary())

# model.compile(optimizer='SDG', loss='mean_squared_error', metrics=['categorical_accuracy'])
# model.fit(x_train, y_train, epochs=10, batch_size=64)

# 2. linear regression

model = LinearRegression()
model.fit(x_train, y_train)
print('\nCoefficient of model: ', model.coef_)
print('\nIntercept of model: ', model.intercept_)
y_pred = model.predict(x_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

# 3. Random trees



