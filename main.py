#This progam makes a table of exp(x) for values to variables from serie de Maclaurin
# exp(x) = 1 + x + x^2/2! + x^3/3! + ...
import math


def ReadRange():
  '''
  This function reads the range of values for the table
  And it returns a tuple with values of xMin, xMax, incN
  '''
  xMin = float(input("Enter the min value of x: "))
  xMax = float(input("Enter the max value of x: "))
  xInc = float(input("Enter the increment of x: "))
  return (xMin, xMax, xInc)
