#!/usr/bin/python

from pysqlite2 import dbapi2 as sqlite
import pandas as pd
#import sys

conn = sqlite.connect('getting_started.db')

with conn:

    cur = conn.cursor()

    cities = (('New York City', 'NY'),
        ('Boston', 'MA'),
        ('Chicago', 'IL'),
        ('Miami', 'FL'),
        ('Dallas', 'TX'),
        ('Seattle', 'WA'),
        ('Portland', 'OR'),
        ('San Francisco', 'CA'),
        ('Los Angeles', 'CA'))
    weather = (('New York City', 2013, 'July', 'January', 62),
        ('Boston', 2013, 'July', 'January', 59),
        ('Chicago', 2013, 'July', 'January', 59),
        ('Miami', 2013, 'August', 'January', 84),
        ('Dallas', 2013, 'July', 'January', 77),
        ('Seattle', 2013, 'July', 'January', 61),
        ('Portland', 2013, 'July', 'December', 63),
        ('San Francisco', 2013, 'September', 'December', 64),
        ('Los Angeles', 2013, 'September', 'December', 75))

    cur.execute("DROP TABLE IF EXISTS cities;")
    cur.execute('CREATE TABLE cities(name text, state text);')
    cur.executemany('INSERT INTO cities (name, state) VALUES(?,?)',cities)

    cur.execute('DROP TABLE IF EXISTS weather;')
    cur.execute('''CREATE TABLE 
        weather(city text, year int, warm_month text, cold_month text, average_high int);''')
    cur.executemany('INSERT INTO weather (city, year, warm_month, cold_month, average_high) VALUES(?,?,?,?,?)', weather)

    var = raw_input("Please enter the month to see the warmest cities in that month: ")

    cur.execute('''SELECT c.name, c.state
                FROM cities c inner join weather w on c.name=w.city
                WHERE w.warm_month = ?
                ;''', (var.capitalize(),))	

    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]	

    df = pd.DataFrame(rows, columns=cols)
    
    
    print "The cities that are warmest in {0} are: ".format(var.capitalize()), 

    # if using data frame, itertuples() can be used for iterating over the rows
    #for row in df.itertuples(): 
    #    print row[1] + ", " + row[2] 

    for row in rows:
    	name, state = row
    	print "{0}, {1},".format(name, state),
