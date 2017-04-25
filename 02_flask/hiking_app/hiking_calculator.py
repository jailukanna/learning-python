#-------------------------------#
#----- Import Dependencies -----#
#-------------------------------#
# `Decimal` library allows us to perform floating point arithmetic
from decimal import Decimal

#-----------------#
#----- Notes -----#
#-----------------#
'''
Calculates hiking travel time based on equation in "The Backpacker's Handbook",
Curtis, Rick, 2005. The equation is as follows:

+ An average hiker on flat terrain has a rate of 30 minutes a mile, or 2 miles per hour.
+ Each hour of elevation gain generally adds 1 hour of additional travel time.
+ Each hour traveled, usually requires at least 5 minutes of stopped rest.
'''
#------------------------#
#----- Improvements -----#
#------------------------#
'''
+ Could validate each form (right now blank submission breaks app)
+ Or validate to make sure that only integers are being added (strings break app also)
+ Refactor
'''

#----------------------------#
#----- Hiking Algorithm -----#
#----------------------------#
# Define our hiking algorithm:
def hiking_time(hike_distance, elevation_gain, rest_time):
    # Calculate # of hours based on elevation gain and total distance:
    raw_time = (Decimal(hike_distance)/Decimal(2)) + (Decimal(elevation_gain)/Decimal(1000)) # calculates number of hours
    print raw_time
    # Calculate total rest time (in minutes), per hour, based on user input:
    rest_time = ((Decimal(hike_distance)/Decimal(2)) + (Decimal(elevation_gain)/Decimal(1000))) * Decimal(rest_time) # calculates rest / # of hours
    # Because rest time is in minutes, convert minutes to hours, round to two decimal places:
    rest_time = round(Decimal(rest_time)/Decimal(60), 2) # `Decimal` is used here for floating point arithmetic
    print rest_time
    # Add the two together for total number of hours:
    total_time = Decimal(raw_time) + Decimal(rest_time)
    # Convert new total to 'hours and minutes' format:
    # First, convert floating value to string:
    str_time = str(total_time)
    # Seperate string at period (to seperate minutes):
    str_time = str_time.split(".", 1)
    hours = str_time[0]
    print hours
    # A lot going on in statement beneath, so to summarize from inside, out:
    # (1) we use `Decimal` to reconvert our string parsing of minutes to a decimal format.
    # (2) we multiply this decimal value by 60 to get minutes in an hour. (instead of fraction of an hour)
    # (3) because we used `Decimal`, we `round` the value (to the tenth's place), and then use `int` to remove the tenths place, leaving a whole number.
    minutes = int(round(Decimal('.' + str_time[1])*60))
    print minutes
    print 'Total Time (in decimal format): ~{} hours'.format(total_time)
    print 'Total Time (in hour & minutes): ~{} hours and {} minutes'.format(hours, minutes)
    return '{} hours and {} minutes'.format(hours, minutes)
