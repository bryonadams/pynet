#!/usr/bin/env python3
##############################################################
# November 23th, 2016                                        #
#  Enter program and prompt user for an IPv4 address. Prompt #
#  until a valid IP is entered.                              #
#    1. Must be IPv4                                         #
#    2. Must contain 4 octets                                #
#    3. First octet must be between 1-223 & cannot be 127    #
#    4. IP address cannot be an APIPA address (169.254/16)   #
#    5. The last three octets must range between 0-255       #
#        (network and broadcast addresses are OK)            #
#   Print the given input when a valid IP is entered.        #
##############################################################

import sys
valid = False

print('Type exit or quit at any time to exit program.')

# Begin loop and get input
while valid == False:
  original = input('Please enter an IPv4 address: ')

  # Leave program without ctrl-c
  if (original == 'exit') or (original == 'quit'):
    print('Bye \n')
    sys.exit()
  
  # Try to convert to integers
  try:
    ip_addr = [int(i) for i in original.split('.')]
  except ValueError:
    print('Invalid characters were entered or an octet is empty, please try again. \n')
    continue
  
  # Determine how many octets were entered
  if len(ip_addr) != 4:
    print('Incorrect number of octets, please try again. \n')
    continue

  # Determine is this is above 223
  if ((ip_addr[0] > 223) and (ip_addr[0] < 256)) or (ip_addr[0] == 0):
    print('First octet is reserved or zero. \n')
    continue

  # Determine if this is a loopback address
  if ip_addr[0] == 127:
    print('I think that was a loopback address, please try again. \n')
    continue 
  
  # Determine if this is an APIPA address
  if (ip_addr[0] == 169) and (ip_addr[1] == 254):
    print('I think that was an APIPA address, please try again. \n')
    continue

  # Determine if the last three octets are between 0-255
  for octet in (ip_addr[1], ip_addr[2], ip_addr[3]):
    if octet in [i for i in range(0,256)]:
      valid = True
    else:
      print('Octet too large or too small, please try again. \n')
      valid = False
      break
    continue

print('The IP address {} is valid.\n'.format(original)) 
