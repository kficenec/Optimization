# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 00:39:18 2017

@author: karen
"""
import numpy as np
from math import sqrt

#lin search goes through each element to find the target. O(N)
def linear_search(F,target):
    #initialize a count, to see how many numbers it checks before finding the answer.
    count = 0
    #loop through the list on each element and return the element if it is your target.
    #also return the count.
    for x in range(len(F)):
        count += 1
        if (F[x] == target):
            returnedList = [x,count]
            return returnedList
    return False

#The section below explains linear search and tests it a little.
print "\nHi! I hope you're having a great day! :) \n"
print "Let's look at the output of some fundamental optimization techniques =D \n"
print "First we will use linear search, which goes through elements in a \
list one-by-one, to find the index of a target item in the list. \n"
print "Using linear_search... \n"
v = [5,7,24,-35,1,76,2,5,6]
t = -35
print "we are examining this list: \n {}".format(v)
print "the target number is {}".format(t)
print "the index (index starts at 0) of target {} is: {}".format(t,linear_search(v,t)[0])
print "We needed to search through {} elements to find this index.\n".format(linear_search(v,t)[1])

print "let's try a few other examples.\n"
v=[54,76,88,90,23,45,82,55,99,32]
t=99
print "list: {} target {}; index: {}".format(v,t,linear_search(v,t)[0])
print "We needed to search through {} elements to find this index.\n".format(linear_search(v,t)[1])

v=[7,2,5,6,3,4,9,12,2,0,7]
t=7
print "list: {} target {}; index: {}".format(v,t,linear_search(v,t)[0])
print "We needed to search through {} elements to find this index.\n".format(linear_search(v,t)[1])
print "\nNotice that in the last example, 7 appeared twice in the list."
print "The linear_search algorithm as it stands will only find the index \
of the first time the number appears in the list.\n"



#use lin search method to find the sqaure root of a number within a tolerance,
#epsilon.

def linearSearch_sqrt(N):
    epsilon = 0.001
    x = 0.000
    while x*x < (N-epsilon):
        x += epsilon
    x = format(x, '.3f')
    return x

#now explain the lin search for square root and show some tests:
print "Now let's use the linear search method to find the square root \
of a number within some tolerance, say epsilon = 0.001\n"
print "The square root of {} is {}\n".format(16,linearSearch_sqrt(16))
print "The square root of {} is {}\n".format(768,linearSearch_sqrt(768))
print "We can check this last one with the built-in python function which \
returns the value of: {}\n".format(sqrt(768))
print "So we are within our desired tolerance (0.001) of the actual root.\n"
print"\n"



#binary search cuts the search space in half with each pass through.

def binarySearch(A, target):
    low = 0
    #b/c indexing starts at zero, you need to subtract 1 
    #from length to get highest index
    high = len(A) - 1 
    #initialize a count to see how many tries it takes to find your answer.
    count = 0
    
    while low <= high: 
        count += 1
        #note python 2.7 / is INTEGER division, 15/2 = 7
        #assess the value of the midpoint...
        mid = low + (high - low) / 2
        #print "LOW {} HI {} MID {}, comparing {} to {}".format(low,high,mid,target,A[mid])
        if A[mid] == target:
            outputVector = [mid,count]
            return outputVector
        #when the midpoint of your sorted list is higher than the target, 
        #change that midpoint to the new highest value that you will search.
        if A[mid] > target:
            high = mid - 1
        #otherwise, the midpoint you examined is too small, so you can set
        #it to the new low of the list you will search.
        else:
            low = mid + 1
            
    #if I want to index all of my answers the same way, I need a 2 item list
    #for when the item is not found as well.
    failedVector = [False, False]
    return failedVector

#explain binary search to users.
print "Now let's use binary search!"
print "By cutting the search space in half with every iteration, \
this search technique will converge on the answer much faster than linear search."
print "In fact it will find it in O(lg(N)) time instead of O(N) time."
print "But the list MUST BE SORTED in order to use this technique :) \n"

    
#make a function that will print all of my test output for me.    
def binSearchPrint(f,t):
    result = binarySearch(f,t)
    print "Looking for [{}] in array {}".format(t,f)
    print "Using binary search, we found our desired number at index {} in \
{} tries.\n".format(result[0], result[1])

#go through some tests of the binary search function.
F = range(10)
target = 6
binSearchPrint(f=F,t=target)

F = range(32)
target = 4
binSearchPrint(f=F,t=target)

#explain tests to users.
F = range(1000000)
target = 129473
result = binarySearch(F,target)
print "Looking for [{}] in an ordered array of one million (numbers are not all \
listed for your viewing convenience).".format(target)
print "Using binary search, we found our desired number at index {} in \
{} tries.".format(result[0], result[1])
print "Wow! just {} tries to find a single value out of one million values!\n".format(result[1])

#check for list where indices don't match numbers
#also remember indices start at zero in python, so 11 is at index 4
print "Let's try an array that is ordered but skips some numbers."
print "Now the index of the desired number will differ from the number itself."
F = [2,5,7,9,11,15,17,27,33,48,55,56,57,58,72,93]
target = 11
binSearchPrint(f=F,t=target)

#check that it handles searching for nonexitent item
print "What happens if we search for a number that is not in our list?"
F = [2,5,7,9,11,15,17,27,33,48,55,56,57,58,72,93]
target = 6
binSearchPrint(f=F,t=target)

#see what happens for a slightly unordered list
#27 should be at index 2, but it's going to look above 17 and cut out 27 on first pass
#will miss the 27 entirely and return false.
print "What happens if the list is slightly unordered?"
print "Notice in the list below that 27 and 17 are out of order."
F = [11,15,27,17,33,48,55,56]
target = 27
binSearchPrint(f=F,t=target)
print "The algorithm did not find 27 because it cut out 27 on the first \
pass as it looks at the numbers greater than 17.  It misses our target number \
entirely.  This shows that the list needs to be sorted for binary search \
to work correctly.\n"

#expected to miss things/ mess up for a very unordered list as well.
#although this is actually returning the correct index sometimes, I guess
#it can HAPPEN to get pushed around in the right direction by chance.
print "Let's mix the a list even more than just one swap..."
from random import shuffle
F = range(12)
shuffle(F)
target = 11
binSearchPrint(f=F,t=target)
print "Sometimes this will happen to work, but most of the time it won't."

print "\n"


#bisection search is like binary search, except for a monotonic function.

def bisection_search_kth_root(n,k):  
    #first float your number to avoid algebra errors down the road.
    N=float(n)
    
    #handle if the user tries to input a zeroth root
    if k==0:
        retrString = "There is no such thing as a zeroth root"
        #the second number is the number of tries taken to find the answer
        return [retrString,0]
    
    
    #a fractional root is actually a power
    if k>0 and k<1:
        kAsPower = 1/k
        power = N**kAsPower
        print "a fractional root is actually a power..."
        #the second number is the number of tries taken to find the answer
        return [power, 1]
    
    #handle negative radicals (including negative fractional radicals)
    negativeRad = False 
    if k<0:
        #neg fractional roots are powers, handle them as such:
        if k > -1:
            k = abs(k)
            ans = 1/(N**(1/k))
            ans = format(ans, '.3f')
            print "A negative fractional root is actually 1 over a power..."
            return [ans,1]
        #neg roots greater than 1 are handled similary to positive roots,
        #except that you need to take the inverse once you find the answer.
        #I will mark negative roots with the negativeRad variable.
        #and later will use that as a cue to take the inverse.
        negativeRad = True
        #until the inverse is taken, the roots need to be normally handled,
        #so I will proceed with the absolute value of k.
        k = abs(k)
        
    
    #handle even roots of negative numbers (which are imaginary)
    #note that this only handles pure imaginary solutions, not complex numbers
    imaginaryNeeded = False
    if k%2==0 and N<0:
        imaginaryNeeded = True
        N=abs(N)
    
    #Next initialize the low and high bounds depending on whether
    #you're finding the root of a positive or negative number
    if N > 0:
        low = 0.0
        high = N
    elif N < 0:
        low = float(n)
        high = 0
    #if N=0, you can just return 0 in 1 try, because any root of zero is zero.
    else: 
        return [0,1]
    
    #set a tolerance level:
    epsilon = 0.001
    
    #loop based on this, when you find the answer change this to true.
    idx = False
    
    #initialize a count so that you know how many iterations it takes to find 
    #the answer.
    count = 0
    
    while not idx:
        count += 1
        midpt = low + (high - low) / 2
        midraised = midpt**k     #** raises something to a higher power
        #print "LOW {} HI {} MID {}, comparing {} to {}".format(low,high,midpt,N,midraised)
        if (midraised >= (N-epsilon)) and midraised <= (N+epsilon):
            idx = True
            #now process special inputs like imaginaries and negative roots.
            if negativeRad == True: 
                midpt = 1/midpt
            midpt = format(midpt, '.3f')
            if imaginaryNeeded == True:
                imaginaryNotation = "The root is imaginary: " + str(midpt) + " i" 
                retrVect = [imaginaryNotation,count]
                return retrVect
            #return the answer and how many iterations it took to find it.
            else:
                retVect = [midpt,count]
                return retVect
        #if the value of the midpoint is too high, then set this to be your new
        #highest value:
        elif midraised > (N+epsilon):
            high = midpt - 0.001
        #if the value of the midpoint is too small, then set this to be your 
        #new lowest value.
        elif midraised < (N-epsilon):
            low = midpt + 0.001
    return False

#explain bisection search to users
print "Now, we'll move onto bisection search."
print "Bisection search is very similar to binary search, except that \
it applies to monotonic (always non-decreasing or non-increasing) functions \
instead of lists of discrete numbers."
print "We will use bisection search to find roots of real or \
imaginary numbers.\n"

#make a function to nicely display the results of tests of bisection search.
def bisectionPrint(root,num):
    if abs(root) == 2:
        suffix = "nd"
    elif abs(root) == 3:
        suffix = "rd"
    else:
        suffix = "th"
    print "The {}{} root of {} is:".format(root,suffix,num)
    bisearch = bisection_search_kth_root(num,root)
    print bisearch[0]
    if bisearch[1] == 1:
        tr = "try"
    else:
        tr = "tries"
    print "We found this in {} {}.".format(bisearch[1],tr)
    print ""

#perform tests of bisection search.
bisectionPrint(root=2,num=9)
bisectionPrint(root=3,num=27)
print "Let's try the root of a negative number!"
bisectionPrint(root=5,num=-3125)
bisectionPrint(root=4,num=0)
bisectionPrint(root=0,num=4)
print "Let's try the roots of some larger numbers."
bisectionPrint(root=7,num=-98876)
bisectionPrint(root=6,num=987576576594)
print "what about imaginary numbers?"
bisectionPrint(root=2,num=-16)

#Try a fractional root which is actually a power.
bisectionPrint(root=0.5,num=4)
print "Can the algorithm handle negative roots?"
bisectionPrint(root=-2,num=4)
print "yes, and it can handle negative fractional roots..."
bisectionPrint(root=-1.0/3.0,num=2)
bisectionPrint(root=1.3,num=2)
bisectionPrint(root=-1.67,num=7)
print "let's try a very high root..."
bisectionPrint(root=75,num=8)
print "bisection search can find the kth root of many numbers \
(but not complex numbers). "

print "\n"



import math 

#make a separate function to find N! (N factorial)
def n_factorial(n):
    n_factori = n*math.log(n,2) - n + 1
    return n_factori

#use bisection search to find argmax of N! for less than a constaint
def bisection_search_lgN(p):
    c = 2**43
    low = 0.0
    high = 0.001
    
    #increase high to a reasonable level given the constraint c.
    while n_factorial(high) < c:
        high = high*2
    
    #loop through and adjust high and low to keep throwing out the half of 
    #the data set where the answer does not live.
    while low <= high:
        #first set N equal to the middle of your bounds.
        N = low + (high-low)/2
        #find n factorial using its function(created above)
        nfacti = n_factorial(N)
        #N should be a whole number, so if N is within 1 that is good.
        if 0 <= (c - nfacti) <= 1:
            N = str(int(N))
            return N
        #if N! is too big, reset the high to the value you just tested for N.
        elif (c - nfacti) < 0:
            high = N - 0.01
        #otherwise N! is too small, so reset low to the value you just tested.
        else:
            low = N + 0.01

print "Now we'll use the bisection search technique to find \
how high N can be for N factorial to be under some value (a constraint)."
print "If we want N! to be less than 1TB, then N can be as high as:"
#note that the input to this isn't used, and so you can throw in whatever you want.
print bisection_search_lgN(54)
print "\n"

# Find sqrt(k) using Newton-raphson method (explained in the print statements below)
def newton_sqrt(k):
    #initialize a count so you know how many iterations it takes.
    count = 0
    #initialize your tolerance level.
    epsilon = .001
    #make an arbitrary guess at the root.
    y = k / 2.0 #guess
    #iterate through while the square root is not within your tolerance.
    while abs(y*y-k) >= epsilon:
        count += 1
        #every time it's not within tolerance, use the Newton-raphson
        #formula to find a better estimate:
        y = y - (((y**2) - k)/(2*y))
    #return the square root and how many iterations it took you to get there.
    rootAndCount = [y,count]
    return rootAndCount

#explain the Newton-Raphson method to users.
print "We'll end with the Newton-Raphson method for finding roots of a polynomial!"
print "The Newton-Raphson method is really interesting..."
print "Picture a polynomial function. You want to find out where it crosses \
the x-axis (as in where y=0)."
print "You make an arbitrary guess and draw the tangent line to the curve \
at this point."
print "You trace down to where the tangent line crosses the x-axis."
print "The zero of this tangent line will be closer to the zero of the \
polynomial than the original point."
print "You now use that zero of the tangent as your new guess, and continue \
the process until you get very close to the actual root."
print "This is an iterative method (because you use each approximation to \
get a better approximation).\n"

#Test the Newton-Raphson method and compare to bisection search efficiency.
newtroot = newton_sqrt(9)
print "With 0.001 tolerance, the Newton sqrt of 9 is: {}".format(newtroot[0])
print "We found this in {} iterations".format(newtroot[1])
print "Compare these {} iterations to the 13 iterations of bisection search \
shown above.".format(newtroot[1])
print "This is an example of the Newton-Raphson method converging \
faster than bisection search, which is generally true.\n"

print "Thanks for reading! :) "







