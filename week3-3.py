###################################################################
# November 18th, 2016                                             #
#  From the given output of "sh ip int brief", create a list      #
#   where each element in the list os a tuple consisting of:      #
#    (interface_name, ip_address, status, protocol).              #
#   Only include interfaces that are up/up and print to           #
#   standard output.                                              #
###################################################################

sh_ip_int_brief = '''
Interface       IP-Address  OK? Method  Status  Protocol
FastEthernet0   unassigned  YES unset   up      up
FastEthernet1   unassigned  YES unset   up      up
FastEthernet2   unassigned  YES unset   down    down
FastEthernet3   unassigned  YES unset   up      up
FastEthernet4   6.9.4.10    YES NVRAM   up      up
NVI0            6.9.4.10    YES unset   up      up
Tunnel1         16.25.253.2 YES NVRAM   up      down
Tunnel2         16.25.253.6 YES NVRAM   up      down
Vlan1           unassigned  YES NVRAM   down    down
Vlan10          10.220.88.1 YES NVRAM   up      up
Vlan20          192.168.0.1 YES NVRAM   down    down
Vlan100         10.220.84.1 YES NVRAM   up      up
'''

# str.splitlines() splits a string on newlines. Equivilent to str.split('\n')
sh_ip_int_brief = sh_ip_int_brief.splitlines()[2:]

# Create newlist 'interfaces' for storage. For each entry in list 'sh_int_int_brief'
#  split the string into a new list stored in 'parts'. If the string 'down' does 
#  not appear in 'parts' append the list to 'interfaces'
interfaces = []
for line in sh_ip_int_brief:
  parts = line.split()
  if 'down' not in parts:
    interfaces.append(parts)

# We don't care about the fields 'OK?' and 'Method', .pop() them off the list
for i in range(len(interfaces)):
  interfaces[i].pop(2)
  interfaces[i].pop(2)

# New lists are created to store the elements of list 'interfaces' so they can 
#  be printed out nicely. Since the position is known I can append specific indexes.
iface, ipv4, status, proto = [], [], [], []
for line in interfaces:
  iface.append(line[0])
  ipv4.append(line[1])
  status.append(line[2])
  proto.append(line[3])

print('{:<15}{:<15}{:<15}{:<15}'.format('Interface', 'IP-Address', 'Status', 'Protocol'))
print('----------------------------------------------------------')
for i, line in enumerate(interfaces):
  print('{:<15}{:<15}{:<15}{:<15}'.format(iface[i], ipv4[i], status[i], proto[i]))
