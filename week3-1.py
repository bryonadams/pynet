#!/usr/bin/env python3
################################################################
# November 16th, 2016                                          #
#  Create a decimal to binary converter for IP addresses.      #
#   A. Make the IP address a command line argument instead of  #
#       prompting for input.                                   #
#   B. Simplify the script logic by using flow control         #
#   C. Zero-pad output to always be 8 binary digits, strip     #
#       off the leading '0b' as well.                          #
#   D. Print to standard output using dotted binary format:    #
#       00001010.01011000.00010001.00010111                    #
################################################################

import sys


# Get IP from input, only 1 argument allowed.
if len(sys.argv) == 2:
  ip_addr = sys.argv.pop()
  ip_bin = ip_addr
  if ip_bin.find(':') >= 1:
    print("This is an IPv6 address. Program takes an IPv4 address.")
    sys.exit()
  ip_bin = ip_bin.split('.')
else:
  if len(sys.argv) == 1:
    print("Too few argument, program accepts an IPv4 address as an argument.")
  else:
    print("Too many arguments, program only takes one IPv4 address.")
  sys.exit()

# ip_bin = [bin(int(i)) for i in ip_bin]  # using list comprehension

# Convert list elements to binary and strip off the leading '0b'
n = 0
for i in ip_bin:
  ip_bin[n] = bin(int(i))[2:]
  n += 1
print(ip_bin)

# Zero pad list elements to be 8 digit binary numbers.
n = 0
for i in ip_bin:
  while len(ip_bin[n]) < 8:
    ip_bin[n] = '0' + ip_bin[n]
  n += 1
print(ip_bin)

ip_bin = '.'.join(ip_bin)

print('{:<15}{:<15}'.format('IP Address', 'Binary'))
print('{:<15}{:<15}'.format(ip_addr, ip_bin))
