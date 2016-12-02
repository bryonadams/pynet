####################################################################
# November 9th, 2016                                               #
# Problem 2-2                                                      #
# Create a script that converts IP addresses                       #
#  from dotted decimal to binary.                                  #
#   1. Prompt user for IP address in dotted                        #
#       decimal format.                                            #
#   2. Convert IP address to binary and display                    #
#       a binary string for each octet:                            #
#       first_octet   second_octet     third_octet    fourth_octet #
#       0b1010        0b1011000        0b1010         0b10011      #
####################################################################

ip4 = input('Please enter an IPv4 address: ')
ip4 = [int(i) for i in ip4.split('.')]

print('{:<15}{:<15}{:<15}{:<15}'.format(ip4[0], ip4[1], ip4[2], ip4[3]))
print('{:<15}{:<15}{:<15}{:<15}'.format(bin(ip4[0]), bin(ip4[1]), bin(ip4[2]), bin(ip4[3])))
