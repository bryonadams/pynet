#########################################################
#  December 10th, 2016                                  #
#   Create a function that returns the multiplication   #
#   product of three parameters: x, y, and z. z should  #
#   have a default value of 1.                          #
#    a. Call the function with all positional           #
#        arguments.                                     #
#    b. Call the function with all named arguments.     #
#    c. Call the function with a mix of positional and  #
#       named arguments.                                #
#    d. Call the function with only two arguments and   #
#       use the default value for z.                    #
#                                                       #
#    Note: Functions stored in pynet_lib.py             #
#                                                       #
#########################################################

# Function, stored in pynet_lib.py
def xyz_mult(x, y, z=1):
  return x * y * z

# Output from interpreter
>>> import pynet_lib
>>> from pynet_lib import xyz_mult

# Part a
>>> xyz_mult(2, 5, 10)
100
# Part b
>>> xyz_mult(x=5, y=5, z=10)
250
# Part c
>>> xyz_mult(5, z=5, y=10)
250
# Part d
>>> xyz_mult(5, 5)
25

