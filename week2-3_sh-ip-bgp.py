###############################################################################
# November 9th, 2016                                                          #
# Using the given four lines from 'show ip bgp'                               #
#  Note, in each case the AS_PATH starts with '701'.                          #
#  Using split() and a list slice, how could you process each                 #
#  of these such that--for each entry, you return an ip_prefix                #
#  and the AS_PATH (the ip_prefix should be a string; the                     #
#  AS_PATH should be a list):                                                 #
#   ip_prefix        as_path                                                  #
#   1.0.192.0/18     ['701', '38040', '9737']                                 #
#   1.1.1.0/24       ['701', '1299', '15169']                                 #
#   1.1.42.0/24      ['701', '9505', '17408', '2.1465']                       #
#   1.0.192.0/19     ['701', '6762', '6762', '6762', '6762', '38040', '9737'] #
###############################################################################

# Given 'show ip bgp'
entry1 = "*  1.0.192.0/18   157.130.10.233     0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24     157.130.10.233     0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24    157.130.10.233     0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233     0 701 6762 6762 6762 6762 38040 9737 i"

# Create lists for each prefix.
entry1     = entry1.split()
entry1.pop()
ip_prefix1 = ''.join(entry1[1:2])
as_path1   = entry1[4:]

entry2     = entry2.split()
entry2.pop()
ip_prefix2 = ''.join(entry2[1:2])
as_path2   = entry2[4:]

entry3     = entry3.split()
entry3.pop()
ip_prefix3 = ''.join(entry3[1:2])
as_path3   = entry3[4:]

entry4     = entry4.split()
entry4.pop()
ip_prefix4 = ''.join(entry4[1:2])
as_path4   = entry4[4:]

print('{:<15}{}'.format('IP Prefix','AS Path'))
print('------------------------')
print('{:<15}{}\n{:<15}{}\n{:<15}{}\n{:<15}{}\n'.format(ip_prefix1, as_path1, ip_prefix2, as_path2, ip_prefix3, as_path3, ip_prefix4, as_path4))

