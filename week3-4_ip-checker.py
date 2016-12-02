#!/usr/bin/env python3
############################################################
# November 20th, 2016                                      #
#  Check the validity of an IP address from input as an    #
#   argument:                                              #
#    1. Must be IPv4                                       #
#    2. Must contain 4 octets                              #
#    3. First octet must be between 1-223 & cannot be 127  #
#    4. IP address cannot be an APIPA address (169.254/16) #
#    5. The last three octets must range between 0-255     #
#        (network and broadcast addresses are OK)          #
#   Print the given input and whether or not it is valid   #
############################################################

import sys

# Get input from argument and end program if number of arguments do not equal 1 
#  and convert the original to a list of integers.
if len(sys.argv) != 2:
  sys.exit('Program takes exactly one argument.\n')
else:
  original = ''.join(sys.argv.pop())

# Note: Exception handling wasn't covered yet in this course. I had previously used 
#  str.isdigit() to determine whether or not each octet contained numbers and then 
#  convertet each index to integers as I went. Converting to integers earlier made
#  the code much cleaner and allows us to check if non-digits are entered at the 
#  same time. 
  try:
    ip_addr = [int(i) for i in original.split('.')]
  except ValueError:
    sys.exit('{} is not a valid IPv4 address.\n'.format(original))

# Determine if this is an IPv4 address by checking for four octets
#  and checking for anything that isn't a digit.
if len(ip_addr) != 4:
  sys.exit('{} is not a valid IPv4 address.\n'.format(original))

# Check if first octet is between 1-223 and is not 127
valid_ip = [i for i in range(1,224)]
valid_ip.remove(127)
if ip_addr[0] not in valid_ip:
  sys.exit('{} is not a valid IPv4 address.\n'.format(original))

# Check if the address is an APIPA address
if (ip_addr[0] == '169') and (ip_addr[1] == 254):
  sys.exit('{} is an APIPA address.\n'.format(original)) 

# The last three octets must be between 0-255. We've already validated the first octet
for octet in (ip_addr[1], ip_addr[2], ip_addr[3]):
  if (octet < 0) or (octet > 255):
    sys.exit('{} is not a valid IPv4 address.\n'.format(original))

print('The IP address {} is valid.\n'.format(original))
