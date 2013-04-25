import MySQLdb
from thermometer4 import read_temp
import os
import time
import datetime

while True:

	now = datetime.datetime.now()
	tempreading = read_temp()
	temperature = tempreading
	try:
		con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
		cur = con.cursor()
		sql_string = "INSERT INTO readings (date_time, temperature) VALUES ('%s', '%s')" % (now,temperature)
		cur.execute(sql_string)
		con.commit()
        except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
	time.sleep(60)
