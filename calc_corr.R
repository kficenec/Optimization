#Group 2-11
#Karen, Lancy, Will & Rob

#clear the workspace & load required packages
rm(list=ls())
installIfAbsentAndLoad <- function(neededVector) {
  for(thispackage in neededVector) {
    if( ! require(thispackage, character.only = T) )
    { install.packages(thispackage)}
    require(thispackage, character.only = T)
  }
}
needed  <-  c("randtests", "RMySQL", "reshape2")      
installIfAbsentAndLoad(needed)

#import the necessary file of nasdaq stocks.
nas <- read.csv("C:\\Users\\karen\\Documents\\Optim\\LastWeekOfClasses\\NasdaqReturns.csv")
#str(nas)

#convert the stock info to a dataframe
nasm <- data.matrix(nas)
#and then take the transpose to get each stock
#as a column (leaving out original columns about
#industry/subindustry information).
nasmt <- t(nasm[,4:123])
#grab the names of the stocks
stockNames <- nas[,1]
#add the stocks as column names
colnames(nasmt) <- stockNames

#Look into time series later
#ts.plot(nasmt[1:119,7])
#choose a row (stock) to examin
#stockCloserLook <- 200
#ts.plot(nasmt[1:119, stockCloserLook])
#abline(h = mean(nasmt[1:119, stockCloserLook]))
#abline(h = HoltWinters(nasmt[1:119, stockCloserLook], 
#                       alpha = NULL, beta = FALSE, gamma = FALSE)$coefficients[1], 
#       lty = 2)
#

#take the mean of the 10 years of stock information
#to get the expected returns.
r <- apply(nasmt, 2, mean)
#make a data frame with the stock names and expected
#returns to be sent to SQL shortly.
rTable <- data.frame("stock" = stockNames, "meanReturn" = r)

#make the covariance matrix of relationships
#betweeen stocks (will also be sent to SQL shortly)
Q <- cov(nasmt)

#put the covariance matrix into pairs of each
#stock. (kind of like converting an adjacency
#matrix to an adjacency list, but with not-sparce data)
Q <- melt(Q)
#names the columns to match what their names are
#in your SQL db.
colnames(Q) <- c("stock1", "stock2", "covariance")

#establish a connection to MySQL db
con <- dbConnect(RMySQL::MySQL(), dbname = 'nasdaq', username = 'root', password = '4572Q*zS7YPt')

#list the tables in the db from SQL
dbListTables(con)

#clear whatever values are currently in the 
#cov and r tables in MySQL because we'll be updating
#them shortly.
dbSendQuery(con, 'truncate table cov')
dbSendQuery(con, 'truncate table r')

#write our covariance & r matrices to MySQL using dbWriteTable.
#warning: errors were returned when our the column names of our cov
#and r dataframes did not match the col names in MySQL.
dbWriteTable(con, value=Q, name = "cov", append = TRUE, row.names =FALSE)
dbWriteTable(con, "r", rTable, append = TRUE, row.names = FALSE)

#We're all done writing to MySQL!  disconnect from it now.
dbDisconnect(con)
