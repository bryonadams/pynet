########################################################
# Library to store functions for PyNet course.         #
#  I'd like to keep the naming convention for my file  #
#  so I made this to dump everything in. This should   #
#  also serve to keep importing simple.                #
#                                                      #
########################################################

# Week 6-1, create a multiplication function. Default value of z is 1
def xyz_mult(x, y, z=1):
  return x * y * z

# Week 6-2, create a dictionary from a given function. Key is the index

def list_dict_conv(a_list):
  '''
  Function converts a list to a dictionary using the index as a key.
  '''
  new_dict = dict(enumerate(a_list))
  return new_dict

# Week 6-3, convert the IP checker from week4-1 to a function.
def ip_checker(ip_address):
  '''
  Takes one IP address and checks whether it is valid or not.
  '''
  # Try to convert to integers
  try:
    ip_addr = [int(i) for i in ip_address.split('.')]
  except ValueError:
    return False
    
  # Determine how many octets were entered
  if len(ip_addr) != 4:
    return False
    
  # Determine if the first octet is valid
  if ((ip_addr[0] > 223) and (ip_addr[0] < 256)) or (ip_addr[0] == 0):
    return False
    
  # Determine if this is a loopback address
  if ip_addr[0] == 127:
    return False
     
  # Determine if this is an APIPA address
  if (ip_addr[0] == 169) and (ip_addr[1] == 254):
    return False
    
  # Determine if the last three octets are between 0-255
  for octet in (ip_addr[1], ip_addr[2], ip_addr[3]):
    if octet not in [i for i in range(0,256)]:
      return False
    else:
      return True
 
# Week 6-4, convert an IP address to binary.
def ip_to_bin(ip_address):
  '''
  Convert an IP address to binary. It calls the previous function, ip_checker() to validate the IP address first.
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









