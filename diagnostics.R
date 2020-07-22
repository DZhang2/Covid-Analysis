setwd("/Users/davidzhang/Desktop/covid-19-data/src")

# training and testing data
testing <- read.csv("TestingData.csv")
training <- read.csv("TrainingData.csv")
par(mfrow=c(2,2))

# histogram and QQ plot
hist(training$new_tests, main="Histogram of Testing Data")
hist(training$new_deaths, main="Histogram of Death Data")
qqnorm(training$new_tests, main="Normal Q-Q Plot Testing")
qqnorm(training$new_deaths, main="Normal Q-Q Plot Deaths")
mtext("Model Diagnostic Plots",side=3, line = -1, outer = TRUE)

# try log transformation
log_deaths = log(training$new_deaths)
hist(log_deaths)
qqnorm(log_deaths, main="Normal Q-Q Plot Log(Deaths)")
