#!/usr/bin/env python3
################################################################
#  December 12th, 2016                                         #
#   Write a program that prompts a user for an IP address,     #
#   then checks if the IP address is valid, and then converts  #
#   the IP address to binary (dotted decimal format). Re-use   #
#   the functions created in exercises 3 and 4 ('import' the   #
#   functions into your new program).                          #
#                                                              #
################################################################

import sys
import pynet_lib
from pynet_lib import ip_checker, ip_to_bin
valid = False

print()
print('Program converts a useful IP address to binary')
print('It does not convert APIPA, loopback, multicast, or reserved addresses.')
print()
while valid == False:
  ipv4 = input('Enter an IPv4 address: ')
  if ip_checker(ipv4) == False:
    print('Bad IP, try again. \n')
    continue
  else:
    valid = True

ipv4_bin = ip_to_bin(ipv4)

print('{:<15}{:<15}'.format('IP Address', 'Binary'))
print('{:<15}{:<15}'.format(ipv4, ipv4_bin))


