##################################################################
# November 9th, 2016                                             #
# Problem 2-1                                                    #
# Create a script that does the following:                       #
#   1. Prompt the user for an IP network                         #
#    a. Assume /24, can be one of the below formats:             #
#       a.b.c.0, a.b.c., a.b.c                                   #
#   2. Store the IP as a list with the below format:             #
#    a. ['a', 'b', 'c', '0']                                     #
#    b. The last octet is always 0.                              #
#   3. Print the IP network out to the screen.                   #
#   4. Print a table that looks like the following,              #
#      columns 20 char width:                                    #
#      NETWORK_NUMBER      FIRST_OCTET_BINARY FIRST_OCTET_HEX    #
#      88.19.107.0         0b1011000          0x58               #
##################################################################

# Getting the IP address and putting it into list
ip4 = input('Please enter a /24 network address: ')
ip4 = ip4.split('.') # Split string into a list
ip4 = ip4[:3]        # Force list to be a /24 network address
ip4.append('0')          
print('{}.{}.{}.{}'.format(ip4[0], ip4[1], ip4[2], ip4[3]))

ip4_str = '.'.join(ip4)
ip4_bin = bin(int(ip4[0]))
ip4_hex = hex(int(ip4[0]))

# Printing the table
print('\n'+'---------------------------------------------------------')
print('%-20s %-20s %-20s' %('NETWORK_NUMBER', 'FIRST_OCTET_BINARY', 'FIRST_OCTET_HEX'))
print('%-20s %-20s %-20s' %(ip4_str, ip4_bin, ip4_hex))
