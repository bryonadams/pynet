#################################################################################
# November 18th, 2016                                                           #
# Simplify week2-3.py using flow control.                                       #
#  week2-3:                                                                     #
#   Using the given four lines from 'show ip bgp'                               #
#    Note, in each case the AS_PATH starts with '701'.                          #
#    Using split() and a list slice, how could you process each                 #
#    of these such that--for each entry, you return an ip_prefix                #
#    and the AS_PATH (the ip_prefix should be a string; the                     #
#    AS_PATH should be a list):                                                 #
#     ip_prefix        as_path                                                  #
#     1.0.192.0/18     ['701', '38040', '9737']                                 #
#     1.1.1.0/24       ['701', '1299', '15169']                                 #
#     1.1.42.0/24      ['701', '9505', '17408', '2.1465']                       #
#     1.0.192.0/19     ['701', '6762', '6762', '6762', '6762', '38040', '9737'] #
#################################################################################

# Given 'show ip bgp'
entry1 = "*  1.0.192.0/18   157.130.10.233     0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24     157.130.10.233     0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24    157.130.10.233     0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233     0 701 6762 6762 6762 6762 38040 9737 i"

entries = [entry1.split(), entry2.split(), entry3.split(), entry4.split()]
prefix  = [entry1.split(), entry2.split(), entry3.split(), entry4.split()]
as_path = [entry1.split(), entry2.split(), entry3.split(), entry4.split()]


# Pull prefix out of prefix list
for i, entries in enumerate(prefix):
  prefix[i] = entries[1]

# Take as_path and strip off the first four and last indices.
for i, entries in enumerate(as_path): 
  as_path[i] = entries[4:-1]


print('{:<15}{}'.format('IP Prefix','AS Path'))
print('------------------------')
n = 0
for i in prefix:
  print('{:<15}{}'.format(prefix[n], as_path[n]))
  n += 1

