# -*- coding: utf-8 -*-
"""
Created on Sat Dec 09 13:41:46 2017

@author: Group 2-11: Karen, Lancy, Will & Rob
"""

from gurobipy import *

m = Model("nasdaqStocks")

m.ModelSense = GRB.MAXIMIZE

#let the model run for about 2 hours
m.setParam('TimeLimit', 7200)

import MySQLdb as mySQL

#dictionary will hold the melted covariance matrix
q = {}
#create a list to hold the values of the returns
r = []
#create a list of the names of the stocks to index 
#the q dictionary on (since cov cols 1 and 2 are 
#the names of the stocks, not indexed numbers)
names = []
    
#initialize a list to hold the percent returns
overallR = []

db =  mySQL.connect(user='root', passwd='4572Q*zS7YPt', 
                    host='localhost', db = 'nasdaq')

cur = db.cursor()
cur.execute('truncate table portfolio')
cur.execute('select * from cov')
for row in cur.fetchall():
    q[(row[0], row[1])] = row[2]
    

cur.execute('select * from r')
for row in cur.fetchall():
    r.append(row[1])
    names.append(row[0])

db.commit()

numStocks = len(r)

a = m.addVars(numStocks, vtype=GRB.CONTINUOUS, name='amounts', lb =0, ub = 1)
m.update()

#constraints
m.addConstr(quicksum(a), GRB.EQUAL, 1, 'InvestAllYouHaveToInvest')
m.update()

#try a bunch of different risks
risk = 0.00
riskLevels = []

for k in range(20):
    risk = risk + 0.025
    m.addConstr(quicksum(a[i] * q[(names[i],names[j])] * a[j] 
    for i in range(numStocks) for j in range(numStocks)), 
    GRB.LESS_EQUAL, risk, 'setRiskLevel')

    m.setObjective(quicksum(a[i]*r[i] for i in range(numStocks))) 
    m.update()
    m.optimize()

    #we can interrogate the result of our model
    #for var in m.getVars():
        #    print var.varname, '=', var.x, '(', var.lb, ',', var.ub, ')'
    if m.status == 2:
        #overallR.append(m.ObjVal)
        #riskLevels.append(risk)
        cur.execute('insert into portfolio values (%s,%s)', (m.ObjVal, risk))
        db.commit()
    print overallR
    m.remove(m.getQConstrs()[0])

db.close()