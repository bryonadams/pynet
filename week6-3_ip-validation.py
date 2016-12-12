#########################################################
#  December 11th, 2016                                  #
#   a. Convert the IP address validation code from      # 
#     week4-1 into a function. Take one variable        #
#     'ip_adress' and return True or False. Include     # 
#     only validation, no prompting for input.          #
#   b. Import the function inot the interpreter and     #
#     test it using both 'import x' and 'from x import  #
#     y' methods.                                       #
#                                                       #
#    Note: Do not run me, I'll kick back errors =)      #
#    Note: Functions stored in pynet_lib.py             #
#                                                       #
#########################################################

# Part a
def ip_checker(ip_address):
  '''
  Takes one IP address and checks whether it is valid or not.
  '''
  # Try to convert to integers
  try:
    ip_addr = [int(i) for i in ip_address.split('.')]
  except ValueError:
    return False
    
  # Determine how many octets were entered
  if len(ip_addr) != 4:
    return False
    
  # Determine if the first octet is valid
  if ((ip_addr[0] > 223) and (ip_addr[0] < 256)) or (ip_addr[0] == 0):
    return False
    
  # Determine if this is a loopback address
  if ip_addr[0] == 127:
    return False
     
  # Determine if this is an APIPA address
  if (ip_addr[0] == 169) and (ip_addr[1] == 254):
    return False
    
  # Determine if the last three octets are between 0-255
  for octet in (ip_addr[1], ip_addr[2], ip_addr[3]):
    if octet not in [i for i in range(0,256)]:
      return False
    else:
      return True

# Part b
>>> import pynet_lib
>>> pynet_lib.ip_checker('192.168.0.1')
The IP address 192.168.0.1 is valid.
True
>>> pynet_lib.ip_checker('127.0.0.1')
I think that was a loopback address, please try again.
False

>>> from pynet_lib import ip_checker
>>> ip_checker('74.75.76.77')
The IP address 74.75.76.77 is valid.
True
>>> ip_checker('169.254.0.1')
I think that was an APIPA address, please try again.
False

