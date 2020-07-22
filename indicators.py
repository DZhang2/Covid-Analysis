import pandas as pd
import numpy as np

def load_file(path):
    file = pd.read_csv(path)
    return file

data = load_file("/Users/davidzhang/Desktop/covid-19-data/public/data/owid-covid-data.csv")
july_20 = data[(data["date"]=="2020-07-20") & (data["total_deaths"]>0)]

# make sure no null data for required factors
july_20 = july_20[(~np.isnan(july_20["median_age"]))]
july_20 = july_20[(~np.isnan(july_20["stringency_index"]))]
july_20 = july_20[(~np.isnan(july_20["population"]))]
july_20 = july_20[(~np.isnan(july_20["aged_70_older"]))]
july_20 = july_20[(~np.isnan(july_20["diabetes_prevalence"]))]
print(len(july_20))

july_20.to_csv("reduced_data.csv")