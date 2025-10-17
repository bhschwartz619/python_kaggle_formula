## Homework #1
## Exercise #1: Kaggle Formula
## Ben Schwartz
## Submission Due: 9/20/25

## Importing in sqrt, log10, e from the math module.
from math import sqrt, log10, e

## 1. User inputs the number of team members, competition rank, and number of teams.
## Make sure the input is valid (positive, non-zero, or whatever).

## User is prompted to input the number of members on the team.
## This value will be stored in the new variable "num_team_members".
num_team_members = int(input("Enter the number of members on your team: "))

## If the input is negative or zero, the while loop will require the user to enter a valid number of members on the
## team (must be a positive, non-zero number).
while num_team_members <= 0:

## This input step (same as line 14) will appear if the value in "num_team_members" is invalid.
    print("Please enter the correct number of members on the team.")
    num_team_members = int(input("Enter the number of members on your team: "))

## User is prompted to input the team's competition rank. This value will be stored in the new variable "comp_rank".
comp_rank = int(input("Enter your team's competition rank: "))

## If the input is negative or zero, the while loop will require the user to enter a valid number for the team's
## competition rank (must be a positive, non-zero number).
while comp_rank <= 0:

## This input step (same as line 25) will appear if the value in "comp_rank" is invalid.
    print("Please enter the team's correct competition rank.")
    comp_rank = int(input("Enter your team's competition rank: "))

## User is prompted to input the number of teams competing in the competition. THis value will be stored in the new
## variable "num_teams".
num_teams = int(input("Enter the number of teams in the competition: "))

## If the input is negative or zero, the while loop will require the user to enter a valid number for the number of
## team's in the competition (must be a positive, non-zero number).
while num_teams <= 0:

## This input step (same as line 37) will appear if the value in "comp_rank" is invalid.
    print("Please enter the correct number of teams in the competition.")
    num_teams = int(input("Enter the number of teams in the competition: "))

# 2. Iterate over number of days since the competition ended by monthly increments, e.g.
# [0, 30, 60, ... 360] days, and compute the awarded competition points.

## Creation of new variables ("days", "upper_limit") to use in the while loop.
days_since = 0
upper_limit = 360

## Creates a while loop to calculate the competition points (values stored in new variable "comp_pts") for every
## increase in 1 month (30 days) since the competition began.
while days_since < upper_limit:

## Runs the inputted values in "num_team_members", "comp_rank", and "num_teams" and the current value stored in
## "days_since" through the Kaggle competition points formula. The output of this function is stored in "comp_pts".
    comp_pts = ((10000/sqrt(num_team_members)) * comp_rank**(-0.75) * log10(1+log10(num_teams))
                * e**((days_since*-1)/500))

##Adds 30 days (1 month) after each iteration
    days_since += 30

# 3. Over each number of days, print the awarded competition points.

## Prints the value in "days_since" and the value in "comp_pts" for each iteration of the while loop
## (each 30-day increment), rounded to the nearest hundredth for cleanliness.
    print("Days since competition:", days_since,",", "Points:",round(comp_pts,2))
