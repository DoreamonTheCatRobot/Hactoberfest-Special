'''
DAVIS STARTCASE

Davis has a number of staircases in his house and he likes to climb each staircase 1, 2, or 3 steps at a time. Being a very precocious child, he wonders how many ways there are to reach the top of the staircase.

Given the heights of a staircas in his house, find and print the number of ways he can climb that staircase.

For example, a staircase in the house that is n=5 steps high. Davis can step on the following sequences of steps:

1 1 1 1 1
1 1 1 2
1 1 2 1 
1 2 1 1
2 1 1 1
1 2 2
2 2 1
2 1 2
1 1 3
1 3 1
3 1 1
2 3
3 2

There are 13 possible ways he can take these 5 steps. 

Function Description

Complete the stepPerms function in the editor below. It should recursively calculate and return the integer number of ways Davis can climb the staircase.

stepPerms has the following parameter(s):

n: an integer, the number of stairs in the staircase
'''
# This is a simple Program solved with Recursion and Dynamic Programming.
# Note: This question can be solved without DP too in O(log n) time.


# This is the main function which will return the final count
def countWaysToClimb(n):
    if n==1:
        # If only one stair is there, only one way exists to climb it i.e. [(1)]
        return 1
    elif n==2:
        # If only two stairs are there, only two ways exists to climb them i.e. [(1,1), (2)]
        return 2
    elif n==3:
        # If only three stairs are there, only four ways exists to climb them i.e. [(1,1,1), (1,2), (2,1), (3)]
        return 4

    # Creation and initialization of list for Memoization. This is the important step for Dynamic Programming.
    dp = [-1]*(n+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    # Call to our recursive function to fill the dp list
    countRecursive(n, dp)

    # Return the answer stored in our list
    return dp[-1]

def countRecursive(n, dp):
    if dp[n] != -1:
        # Return the value if already calculated (This reduces our computation time in the cost of space)
        return dp[n]
    # If value is -1 then calculate the value Recursively.
    dp[n] = countRecursive(n-3, dp) + countRecursive(n-2, dp) + countRecursive(n-1, dp)
    return dp[n]

n = int(input("Enter number of stairs: "))
print(countWaysToClimb(n))