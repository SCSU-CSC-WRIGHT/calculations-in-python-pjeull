import math

principal = input("Please insert the principal amount: ")
rate = input("Please insert the rate: ")
period = input("Please insert the time period (in years): ")

simple_interest = (int(principal)*int(rate)*int(period))/100

print("The simple interest is ", simple_interest)