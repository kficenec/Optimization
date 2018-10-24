# Optimization

In the optimization course in the MSBA program at the college of William & Mary, I developed non-linear and linear programming skills and discrete optimization techniques. Using programs as accessible as Excel to more complex languages and tools such as Python and Gurobi, I applied these skills to optimize transportation routes, maximize profit, assess risk and more.

# Summary of work

## hw2 - graph theory
uses an R markdown file to answer questions about graph theory and applications, including adjacency matrix to list conversion, generating a minimum spanning tree, and applying shortest path algorithms to project scheduling. 

## hw3 - linear programming
uses Excel to maximize earnings for companies given supply/demand constraints. Sensitivity analysis on the robustness of the optimal solution is also performed in the event that predicted supply or demand is off.

## HW4 - linear programming part 2
uses Excel to solve linear optimization problems. Problem 9.3 finds the optimal placement of ATM machines to reduce drivetime for the customers of a bank. Problem 9.4 involves optimizing a TV schedule given constraints of the network to show certain programs. Problem 9.7 balances the cost/benefit of producing certain types of trucks at a production facility that can only produce one type of product each month and optimizes revenue under these constraints. And problem 9.8 optimizes the selection of a student's college courses given prerequisite and course requirement constraints. 

## Maximize Return on Stock Portfolio (set of files: calc_corr.R, portfolio.py, writeup.rmd, writeup.pdf)

These were part of a group assignment to maximize stock portfolio return given certain acceptible risk levels of the client.

calc_corr takes raw information about NASDAQ stock returns and calculates the relationship between different stocks in the form of a covariance matrix (it also writes this information from R to SQL using the RMySQL package). Just like you wouldn't want to put all your money into one stock, you wouldn't want to put all your money into a group of stocks that tend to rise and fall together, that is why the covariance of the stocks is important. 

portfolio.py uses python and Gurobi to optimize investment in stocks given different levels of acceptible risk. I also practiced python to SQL communication in this file.

writeup.rmd is the R markdown file with the associated pdf that shows the results being read back into R and the graphical output of return vs. risk for the optimal NASDAQ stock portfolio investment.
