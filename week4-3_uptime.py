#!/usr/bin/env python3
###################################################
# November 26, 2016                               #
#  Create a program that converts the given       #
#   uptime strings to a time in seconds. Store    #
#   the uptime in a dictionary using the device   #
#   name as the hostname. Print the dictionary to #
#   standard output.                              #
#                                                 #
###################################################

minute_secs = 60 
hour_secs   = minute_secs * 60 
day_secs    = hour_secs * 24
week_secs   = day_secs * 7
year_secs  = day_secs * 365


# Given uptime strings
uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

# Create empty dictionary to store uptime
uptime_dict = {}

# Uptime 1 
# Filter out data for uptime1
hostname1 = uptime1.split(' ')[0]
time1_str = uptime1.split('is')[1].split(',')
time1 = [i[1:] for i in time1_str]

# Convert time to integers
seconds_up = 0
for part in time1:
  if 'year' in part:
    years = []
    for i in part:
      if i.isdigit() == True:
        years.append(i)
    seconds_up += (int(''.join(years)) * year_secs)
  if 'week' in part:
    weeks = []
    for i in part:
      if i.isdigit() == True:
        weeks.append(i)
    seconds_up += (int(''.join(weeks)) * week_secs)
  if 'day' in part:
    days = []
    for i in part:
      if i.isdigit() == True:
        days.append(i)
    seconds_up += (int(''.join(days)) * day_secs)
  if 'hour' in part:
    hours = []
    for i in part:
      if i.isdigit() == True:
        hours.append(i)
    seconds_up += (int(''.join(hours)) * hour_secs)
  if 'minute' in part:
    minutes = []
    for i in part:
      if i.isdigit() == True:
        minutes.append(i)
    seconds_up += (int(''.join(minutes)) * minute_secs)

uptime_dict[hostname1] = seconds_up 

# Uptime 2
# Filter out data for uptime1
hostname2 = uptime2.split(' ')[0]
time2_str = uptime2.split('is')[1].split(',')
time2 = [i[1:] for i in time2_str]

# Convert time to integers
seconds_up = 0
for part in time2:
  if 'year' in part:
    years = []
    for i in part:
      if i.isdigit() == True:
        years.append(i)
    seconds_up += (int(''.join(years)) * year_secs)
  if 'week' in part:
    weeks = []
    for i in part:
      if i.isdigit() == True:
        weeks.append(i)
    seconds_up += (int(''.join(weeks)) * week_secs)
  if 'day' in part:
    days = []
    for i in part:
      if i.isdigit() == True:
        days.append(i)
    seconds_up += (int(''.join(days)) * day_secs)
  if 'hour' in part:
    hours = []
    for i in part:
      if i.isdigit() == True:
        hours.append(i)
    seconds_up += (int(''.join(hours)) * hour_secs)
  if 'minute' in part:
    minutes = []
    for i in part:
      if i.isdigit() == True:
        minutes.append(i)
    seconds_up += (int(''.join(minutes)) * minute_secs)

uptime_dict[hostname2] = seconds_up

# Uptime 3
# Filter out data for uptime1
hostname3 = uptime3.split(' ')[0]
time3_str = uptime3.split('is')[1].split(',')
time3 = [i[1:] for i in time3_str]

# Convert time to integers
seconds_up = 0
for part in time3:
  if 'year' in part:
    years = []
    for i in part:
      if i.isdigit() == True:
        years.append(i)
    seconds_up += (int(''.join(years)) * year_secs)
  if 'week' in part:
    weeks = []
    for i in part:
      if i.isdigit() == True:
        weeks.append(i)
    seconds_up += (int(''.join(weeks)) * week_secs)
  if 'day' in part:
    days = []
    for i in part:
      if i.isdigit() == True:
        days.append(i)
    seconds_up += (int(''.join(days)) * day_secs)
  if 'hour' in part:
    hours = []
    for i in part:
      if i.isdigit() == True:
        hours.append(i)
    seconds_up += (int(''.join(hours)) * hour_secs)
  if 'minute' in part:
    minutes = []
    for i in part:
      if i.isdigit() == True:
        minutes.append(i)
    seconds_up += (int(''.join(minutes)) * minute_secs)

uptime_dict[hostname3] = seconds_up

# Uptime 4
# Filter out data for uptime1
hostname4 = uptime4.split(' ')[0]
time4_str = uptime4.split('is')[1].split(',')
time4 = [i[1:] for i in time4_str]

# Convert time to integers
seconds_up = 0
for part in time4:
  if 'year' in part:
    years = []
    for i in part:
      if i.isdigit() == True:
        years.append(i)
    seconds_up += (int(''.join(years)) * year_secs)
  if 'week' in part:
    weeks = []
    for i in part:
      if i.isdigit() == True:
        weeks.append(i)
    seconds_up += (int(''.join(weeks)) * week_secs)
  if 'day' in part:
    days = []
    for i in part:
      if i.isdigit() == True:
        days.append(i)
    seconds_up += (int(''.join(days)) * day_secs)
  if 'hour' in part:
    hours = []
    for i in part:
      if i.isdigit() == True:
        hours.append(i)
    seconds_up += (int(''.join(hours)) * hour_secs)
  if 'minute' in part:
    minutes = []
    for i in part:
      if i.isdigit() == True:
        minutes.append(i)
    seconds_up += (int(''.join(minutes)) * minute_secs)

uptime_dict[hostname4] = seconds_up

for i in uptime_dict:
  print('{:<15} {}'.format(i, uptime_dict.get(i))) 
