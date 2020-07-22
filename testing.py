import pandas as pd
import matplotlib.pyplot as plt

def load_file(path):
    file = pd.read_csv(path)
    return file

n = 2.5
mortality_rate = 0.0125
# estimated parameters
data = load_file("/Users/davidzhang/Desktop/covid-19-data/public/data/owid-covid-data.csv")
us = data[(data["location"]=="United States") & (data["new_tests"]>0)]
us["Percent Positivity"] = us["new_cases"]/us["new_tests"]*100
us["IFR^"] = us["total_deaths"]/us["total_cases"]*100
us["Positivity Standardized Cases"] = us["new_cases"] * us["Percent Positivity"] / n
us["Mortality Standardized Cases"] = us["new_deaths"] / mortality_rate
us["Mortality Standardized Total"] = us["total_deaths"] / mortality_rate
us["Estimated Percent Infected"] = us["Mortality Standardized Total"]/us["population"]*100
us = us[["date", "new_cases", "new_deaths", "new_tests", "total_cases", "total_deaths", "IFR^", "Percent Positivity", "Positivity Standardized Cases", "Mortality Standardized Cases",
        "Mortality Standardized Total", "Estimated Percent Infected"]]
us.to_csv("USData.csv")
recent = us.tail(30)

# positivity standardization changes by increasing % population infected
#   based on variance in relation to n, the metric underestimate/overestimates
#   underestimated when actual n < 2.5% and underestimates when n > 2.5%

# Mortality standardization depends heavily on ifr and its estimated value which can change (estimated at 0.4-2) high low prob
#   depending on treatment, vaccine, hospitilization, etc...
# Death counts are also crucial and a lagging indicator by ~1-2 weeks (or mean time it takes for virus to kill)
# Counting of deaths may be over or under estimated or confounded with other pre-existing conditions
#   however; if counting remains relatively consistent, increases/decreases in cases can be assessed

# plt.plot(us["Percent Positivity"], label='standardized cases')
# plt.title('Cases/Tests')
# plt.show()

avg = 0.792
df = pd.DataFrame({"avg": avg, "IFR": us["IFR^"]})
plt.plot("IFR", data=df, label="IFR from data")
plt.plot("avg", data=df, label="Actual estimated IFR")
plt.legend()
plt.title("Calculated IFR")
# plt.show()

