import datetime 
import time

GIGASECOND = 1e9

def add_gigasecond(birth_date):
    birth = time.mktime((birth_date).timetuple())
    gig_time = birth + GIGASECOND
    return datetime.datetime.fromtimestamp(gig_time)

"""
import datetime

GIGASECOND = datetime.timedelta(seconds=1e9)

def add_gigasecond(birth_date):
    return birth_date + GIGASECOND
"""