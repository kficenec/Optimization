# Optimization

In the optimization course in the MSBA program at the college of William & Mary, I solved non-linear and linear programming problems and practiced discrete optimization techniques by utilizing tools such as Excel, Python and Gurobi. I applied these skills to optimize transportation routes, maximize profit, assess risk, schedule projects and more.

You can use these files to teach yourself some optimization techniques. If you understand the concepts well enough, you can even change input values or paramters to solve a problem at your own company or in your day-to-day life.

# Contents

## Maximize Return on Stock Portfolio (set of files: calc_corr.R, portfolio.py, writeup.rmd, writeup.pdf, nasdaqReturns.csv)

These files show how to maximize stock portfolio return given certain acceptible risk levels of a client.

calc_corr takes raw information about NASDAQ stock returns (from nasdaqReturns.csv) and calculates the relationship between different stocks in the form of a covariance matrix; it also writes this information from R to SQL using the RMySQL package. Just like you wouldn't want to put all your money into one stock, you wouldn't want to put all your money into a group of stocks that tend to rise and fall together, that is why the covariance of the stocks is important. 

portfolio.py uses python and Gurobi (and the covariance information just created) to optimize investment in stocks given different levels of acceptible risk. It also displays how to communicate between Python and MySQL.

writeup.rmd is the R markdown file with the associated pdf that shows the results being read back into R and the graphical output of return vs. risk for the optimal NASDAQ stock portfolio investment.

Note that you can use this strategy and code for any investment portfolio of interest. 

## Graph theory (graphTheory.rmd, graphTheory.pdf)

Using R markdown, I apply graph theory concepts to convert adjacency matrices to lists, generate a minimum spanning tree, and apply shortest path algorithms to project scheduling. 

How you can use this:

The minimum spanning tree has some interesting applications. For example, after the hurricane in Puerto Rico, crews needed to clear roads so that people and supplies could be transported; however, you can connect every house/store/etc. without clearing every single road (picture a grid structure with 2 points on diagonal corners...you can clear a single root between the 2 points, and don't need to clear every single segment). The minimum spanning tree would show you how to clear the minimum about of road in order to connect all your points. Kruskal's algorithm is implemented to solve this using the function msTreeKruskal in R. This function is very easy to use as long as you give it distances (or weights between nodes) in terms an an adjacency list. An adjacency list tells you the start point, the end point, and the distance (or weight) between them.  If you start with an adjacency matrix (a matrix of the distances between all points), then the first part of this markdown file will convert that into an adjacency list for you. For this example, you could list a weight as how much money is would cost to clear that road instead of how long the road is, and then the minimum spanning tree would tell you how to connect all places for the minimum cost.

The second usage of minimum spanning tree is given as a thought experiment, and it explains how to find a maximum  of products instead of a minimum sum of the graph edges. For this example, we wanted to maximize the probability of a safe transfer of information between government agents in a foreign country. You could apply this concept to any set of points/people/things you want to connect that have some probability of interest. 

## Linear programming
uses Excel to maximize earnings for companies given supply/demand constraints. Sensitivity analysis on the robustness of the optimal solution is also performed in the event that predicted supply or demand is off.

## Linear programming part 2
uses Excel to solve linear optimization problems. Problem 9.3 finds the optimal placement of ATM machines to reduce drivetime for the customers of a bank. Problem 9.4 involves optimizing a TV schedule given constraints of the network to show certain programs. Problem 9.7 balances the cost/benefit of producing certain types of trucks at a production facility that can only produce one type of product each month and optimizes revenue under these constraints. And problem 9.8 optimizes the selection of a student's college courses given prerequisite and course requirement constraints. 

## Search Functions (LinearBinaryAndBisectionSearch.py)

With this python code, I implemented different search functions and tested their robustness. This code is written with many comments and text outputs to clearly communicate these concepts to someone unfamiliar with them - so you can learn about these search functions if you've never seen them before! :) First I show linear search which is very inefficient; this serves as motivation for why you would want to select a more intelligent search function. Next I walk through binary and bisection search which perform much better. I conclude with a brief description and example of the Newton-Raphson method.
