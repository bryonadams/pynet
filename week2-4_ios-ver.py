###############################################################
# November 10th, 2016                                         #
#  You have the given string from "show version"              #
#    on a Cisco router. The string is a single line,          #
#    how would you process the string to only receive         #
#    the IOS version?                                         #
#     Version:                                                #
#      ios_version = "15.0(1)M4"                              #
#                                                             #
###############################################################

# Given string for Cisco IOS version
cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"

ios_version = cisco_ios.split(' ')
ios_version = (ios_version[(ios_version.index('Version') + 1)]) # IOS version is after the word "Version"
ios_version = ios_version[:-1] # Remove the comma
print(ios_version)


# Given string for Cisco IOS version
cisco_ios = "Cisco IOS Software, s72033_rp Software (s72033_rp-ADVENTERPRISEK9_WAN-M), Version 12.2(33)SXJ10, RELEASE SOFTWARE (fc3)"

ios_version = cisco_ios.split(' ')
ios_version = (ios_version[(ios_version.index('Version') + 1)]) # IOS version is after the word "Version"
ios_version = ios_version[:-1] # Remove the comma
print(ios_version)


# Given string for Cisco IOS version
cisco_ios = "Cisco IOS Software, ASR1000 Software (X86_64_LINUX_IOSD-ADVENTERPRISEK9-M), Version 15.4(3)S5a, RELEASE SOFTWARE (fc2)"

ios_version = cisco_ios.split(' ')
ios_version = (ios_version[(ios_version.index('Version') + 1)]) # IOS version is after the word "Version"
ios_version = ios_version[:-1] # Remove the comma
print(ios_version)
