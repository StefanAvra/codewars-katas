"""
Human readable duration format

Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.


"""

def format_duration(seconds):
    minute = 60
    hour = minute * 60
    day = hour * 24
    year = day * 365
    friendly = []
    if seconds >= year:
        years = int(seconds / year)
        seconds -= years * year
        friendly.append(f'{years} year{"s" if years > 1 else ""}')
    if seconds >= day:
        days = int(seconds / day)
        seconds -= days * day
        friendly.append(f'{days} day{"s" if days > 1 else ""}')
    if seconds >= hour:
        hours = int(seconds / hour)
        seconds -= hours * hour
        friendly.append(f'{hours} hour{"s" if hours > 1 else ""}')
    if seconds >= minute:
        minutes = int(seconds/ minute)
        seconds -= minutes * minute
        friendly.append(f'{minutes} minute{"s" if minutes > 1 else ""}')
    if seconds:
        friendly.append(f'{seconds} second{"s" if seconds > 1 else ""}')
    if len(friendly) == 1:
        return friendly[0]
    elif len(friendly) == 0:
        return 'now'
    else:
        return ', '.join(friendly[:-1]) +' and '+ friendly[-1]
