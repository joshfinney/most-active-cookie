import random
import datetime
import csv

"""
Generates mock cookie log
• 5 different cookie strings
• Each log is a randomly chosen from the cookie string set
• 5 cookie logs a day from a month ago to today
"""

def generate_random_cookie():
    """Generates a random cookie string."""
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=16))

def generate_cookie_set(num_cookies=5):
    """Generates a set of unique cookies."""
    return {generate_random_cookie() for _ in range(num_cookies)}

def generate_timestamps(start_date, num_days, cookies_per_day):
    """Generates timestamps for each cookie entry over a number of days."""
    return [start_date + datetime.timedelta(days=day, minutes=minute) 
            for day in range(num_days) 
            for minute in range(0, cookies_per_day * 60, 60)]

def create_cookie_log(filename, start_date, num_days=30, cookies_per_day=5):
    """Creates a cookie log file with random data."""
    timestamps = generate_timestamps(start_date, num_days, cookies_per_day)
    cookies = generate_cookie_set(cookies_per_day)

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['cookie', 'timestamp'])
        for timestamp in timestamps:
            writer.writerow([random.choice(list(cookies)), timestamp.isoformat()])

end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=30)

create_cookie_log('cookie_log.csv', start_date)