import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def load_file(path):
    file = pd.read_csv(path)
    return file

us = load_file("./Data/USData.csv")
recent = us.tail(37)
training = recent.head(30)
testing = recent.tail(7)

deaths = training["new_deaths"]
deaths = np.log(deaths)
tests = training["new_tests"]
xBar = np.mean(deaths)
sigma = np.std(deaths, ddof=1)
xBar2 = np.mean(tests)
sigma2 = np.std(tests, ddof=1)
print(xBar, sigma) 
print(xBar2, sigma2) 
testing["new_deaths"] = np.log(testing["new_deaths"])
testing_data = testing[["new_tests", "new_deaths"]]
training_data = training[["new_tests", "new_deaths"]]
testing_data.to_csv("./Data/TestingData.csv")
training_data.to_csv("./Data/TrainingData.csv")
