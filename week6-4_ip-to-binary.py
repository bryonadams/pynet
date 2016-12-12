###########################################################
#  December 12th, 2016                                    #
#   Create a function using the dotted decimal to binary  #
#   program from week3-1. Do not prompt for inputer and   #
#   do not print to standard output. The function should  #
#   take 'ip_address' and return the IP in dotted binary  #
#   format padded to 8 digits. You may wish to create     #
#   other functions as well, such as the zero padding.    #
#                                                         #
#    Note: Do not run me, I'll kick back errors =)        #
#    Note: Functions stored in pynet_lib.py               #
#    Note: I chose not to create an extra function for 0  #
#          padding the binary octets. Seemed unnecessary  # 
#                                                         #
###########################################################

def ip_to_bin(ip_address):
  '''
  Convert an IP address to binary.
  '''
  # Convert the IP address to a list
  octets = [bin(int(octet)) for octet in ip_address.split('.')]

  # Convert list of octets to 0 padded 8 digit binary without the leading '0b'
  n = 0
  for octet in octets:
    octets[n] = octet[2:]
    while len(octets[n]) < 8:
      octets[n] = '0' + octets[n]
    n += 1

  return '.'.join(octets)


# Output from interpreter
>>> import pynet_lib
>>> from pynet_lib import *
>>> ip_to_bin('192.168.0.1')
'11000000.10101000.00000000.00000001'

