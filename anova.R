setwd("/Users/davidzhang/Desktop/covid-19-data/src")

data <- read.csv("reduced_data.csv")
attach(data)

#test different indicator impacts
#code indicators for easier reference
r1a = total_deaths
r2a = total_cases
r1b = total_deaths_per_million
r2b = total_cases_per_million
a = stringency_index
b = population
c = diabetes_prevalence
d = aged_70_older
e = total_tests_per_thousand
f = gdp_per_capita
g = hospital_beds_per_thousand


a1 = aov(r1a ~ a * b * c)
summary(a1)
print(a1)
a2 = aov(r1b ~ a * b * c)
summary(a2)
