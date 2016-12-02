#!/usr/bin/env python3
################################################################
# November 24, 2016                                            #
#  Take the given string for 'show version' on a Cisco router  #
#  and return the following information:                       #
#   vendor, model, os_version, uptime, serial number           #
#  Code should be generic and work on other versions.          #
#                                                              #
################################################################

sh_ver = '''
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)
twb-sf-881 uptime is 7 weeks, 5 days, 19 hours, 23 minutes
System returned to ROM by reload at 15:33:36 PST Fri Feb 28 2014
System restarted at 15:34:09 PST Fri Feb 28 2014
System image file is "flash:c880data-universalk9-mz.150-1.M4.bin"
Last reload type: Normal Reload
Last reload reason: Reload Command
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX1000038X
5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
License Info:
License UDI:
-------------------------------------------------
Device#   PID                   SN
-------------------------------------------------
*0        CISCO881-SEC-K9       FTX1000038X
License Information for 'c880-data'
    License Level: advipservices   Type: Permanent
    Next reboot license Level: advipservices
Configuration register is 0x2102
'''
import sys

# New empty dictionary to store information.
router_dict = {}

# Get vendor, although we know it's Cisco anyway.
if 'Cisco' in sh_ver:
  router_dict['vendor'] = 'Cisco'
else:
  sys.exit('This is not a Cisco device')

# Split sh ver output to a list of lines
ver_lines = sh_ver.split('\n')

for line in ver_lines:
 
# Get the IOS version, this parses for the string 'Cisco IOS Software', 
#  in every line in 'ver_lines.' It then splits the string and returns 
# position 2 as the os version and strips off the leading space.
  if 'Cisco IOS Software' in line:
    router_dict['os_ver'] = line.split(',')[2][1:]

# Get the model of router using the same logic as the IOS version. The line
#  doesn't have a nice split character so I rebuilt the string using spaces.
  if 'bytes of memory' in line:
    router_dict['model'] = ' '.join(line.split()[0:3])

# Get uptime using the same logic as 'model'
  if 'uptime' in line:
    router_dict['uptime'] = ' '.join(line.split()[3:])

# Get serial number using the logic from 'os_ver'
  if 'Processor board ID' in line:
    router_dict['serial'] = line.split()[3]

for i in router_dict:
  print('{:<10} {}'.format(i, router_dict.get(i)))
