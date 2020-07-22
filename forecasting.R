setwd("/Users/davidzhang/Desktop/covid-19-data/src")
testing <- read.csv("TestingData.csv")
training <- read.csv("TrainingData.csv")
# par(mfrow=c(3,1))

log_deaths = log(training$new_deaths)
tests = training$new_tests

# transform to time series data
log_deaths = ts(log_deaths, frequency=7)
tests = ts(tests, frequency = 7)

# single, double, and triple EWMA analysis
library(stats)
ewma1t = HoltWinters(tests, beta=FALSE, gamma=FALSE)
ewma2t = HoltWinters(tests, beta=FALSE)
ewma3t = HoltWinters(tests)
ewma1d = HoltWinters(log_deaths, beta=FALSE, gamma=FALSE)
ewma2d = HoltWinters(log_deaths, beta=FALSE)
ewma3d = HoltWinters(log_deaths)

# print parameter and coefficient results
ewma1t
ewma2t
ewma3t
ewma1d
ewma2d
ewma3d

# getting fitted values
ewma1t_fit = ewma1t$fitted
ewma2t_fit = ewma2t$fitted
ewma3t_fit = ewma3t$fitted
ewma1d_fit = ewma1d$fitted
ewma2d_fit = ewma2d$fitted
ewma3d_fit = ewma3d$fitted
#plot(ewma1t_fit)
#plot(ewma2t_fit)
#plot(ewma3t_fit)
#plot(ewma1d_fit)
#plot(ewma2d_fit)
#plot(ewma3d_fit)

# getting forecasts
fore1t = predict(ewma1t, 7, prediction.interval=TRUE)
fore2t = predict(ewma2t, 7, prediction.interval=TRUE)
fore3t = predict(ewma3t, 7, prediction.interval=TRUE)
fore1d = predict(ewma1d, 7, prediction.interval=TRUE)
fore2d = predict(ewma2d, 7, prediction.interval=TRUE)
fore3d = predict(ewma3d, 7, prediction.interval=TRUE)
# plot(fore1t)

actual_testing = testing$new_tests
actual_deaths = testing$new_deaths
TD_t1 = cbind(actual_testing, fore1t)
TD_t2 = cbind(actual_testing, fore2t)
TD_t3 = cbind(actual_testing, fore3t)
TD_d1 = cbind(actual_deaths, fore1d)
TD_d2 = cbind(actual_deaths, fore2d)
TD_d3 = cbind(actual_deaths, fore3d)

Days = c(1:7)

#plot forecasts
matplot(Days, TD_t1, pch=c(1:4), col=c(1:4), pch=c(1:4), col=c(1:4), type="b", xlab="Days", ylab="New Tests", main="Single EWMA Tests")
  legend("topleft", legend=c("Data", "Forecast", "Upper bound", "Lower bound")
         , col=c(1:4), pch=c(1:4))
		 
matplot(Days, TD_t2, pch=c(1:4), col=c(1:4), type="b", xlab="Days", ylab="New Tests", main="Double EWMA Tests")
  legend("topleft", legend=c("Data", "Forecast", "Upper bound", "Lower bound")
         , col=c(1:4), pch=c(1:4))

matplot(Days, TD_t3, pch=c(1:4), col=c(1:4), type="b", xlab="Days", ylab="New Tests", main="Triple EWMA Tests")
  legend("topleft", legend=c("Data", "Forecast", "Upper bound", "Lower bound")
         , col=c(1:4), pch=c(1:4))

matplot(Days, TD_d1, pch=c(1:4), col=c(1:4), type="b", xlab="Days", ylab="New Deaths", main="Single EWMA Deaths")
  legend("topleft", legend=c("Data", "Forecast", "Upper bound", "Lower bound")
         , col=c(1:4), pch=c(1:4))

matplot(Days, TD_d2, pch=c(1:4), col=c(1:4), type="b", xlab="Days", ylab="New Deaths", main="Double EWMA Deaths")
  legend("topleft", legend=c("Data", "Forecast", "Upper bound", "Lower bound")
         , col=c(1:4), pch=c(1:4))

matplot(Days, TD_d3, pch=c(1:4), col=c(1:4), type="b", xlab="Days", ylab="New Deaths", main="Triple EWMA Deaths")
  legend("topleft", legend=c("Data", "Forecast", "Upper bound", "Lower bound")
         , col=c(1:4), pch=c(1:4))
