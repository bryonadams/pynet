#########################################################
#  December 11th, 2016                                  #
#   Write a function that converts a list to a          #
#   dictionary where the index of the list is used as   #
#   the key to the new dictionary. Function should      #
#   return the new dictionary.                          #
#                                                       #
#    Note: Do not run me, I'll kick back errors =)      #
#    Note: Functions stored in pynet_lib.py             #
#                                                       #
#########################################################

def list_dict_conv(a_list):
  '''
  Function converts a list to a dictionary using the index as a key.
  '''
  new_dict = dict(enumerate(a_list))
  return new_dict




# Function output from interpreter
>>> temp = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> list_dict_conv(temp)
{0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g'}


