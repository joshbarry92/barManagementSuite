import MySQLdb
import serial
import os
import time
import datetime

ser = serial.Serial('/dev/ttyACM0', 115200)


def insert_Coronita():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Coronita","-275",now,"RFID")
	cur.execute(sql_string)
	con.commit()
	
def insert_SoleStar():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Winter Zest","-330",now,"RFID")
	cur.execute(sql_string)
	con.commit()


while True:
	message = ser.readline()
	mes = message[0:4]
	print(mes)
	if mes == '6687' :
		insert_Coronita()
		os.system("mpg321 beep-7.mp3")
		print("Coronita Updated")
	elif mes == '7087' :
		insert_SoleStar()
		os.system("mpg321 beep-7.mp3")
		print("Winter Zest Updated")
	else:
		time.sleep(0.5)
	time.sleep(0.5)

