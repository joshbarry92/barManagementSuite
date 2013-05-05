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
	
def insert_WinterZest():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Winter Zest","-330",now,"RFID")
	cur.execute(sql_string)
	con.commit()
	
def insert_Guinness():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Guinness","-500",now,"RFID")
	cur.execute(sql_string)
	con.commit()
	
def insert_ToffeeAppleCider():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Toffee Apple Cider","-500",now,"RFID")
	cur.execute(sql_string)
	con.commit()

def insert_Carlsberg():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Carlsberg","-440",now,"RFID")
	cur.execute(sql_string)
	con.commit()

def insert_OriginalAppleCider():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Original Apple Cider","-500",now,"RFID")
	cur.execute(sql_string)
	con.commit()
	
def insert_BittersweetAppleCider():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Bittersweet Apple Cider","-500",now,"RFID")
	cur.execute(sql_string)
	con.commit()
	
def insert_TuttiFruttiPearCider():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Tutti Frutti Pear Cider","-500",now,"RFID")
	cur.execute(sql_string)
	con.commit()
	
def insert_StrawberryCider():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Strawberry Cider","-500",now,"RFID")
	cur.execute(sql_string)
	con.commit()
	
def insert_DoubleChocolateStout():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Double Chocolate Stout","-500",now,"RFID")
	cur.execute(sql_string)
	con.commit()
	
def insert_Stella4():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Stella 4","-440",now,"RFID")
	cur.execute(sql_string)
	con.commit()
	
def insert_Stella():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Stella","-500",now,"RFID")
	cur.execute(sql_string)
	con.commit()
	
def insert_SoleStar():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Sole Star","-500",now,"RFID")
	cur.execute(sql_string)
	con.commit()
	
def insert_SummerZest():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Summer Zest","-330",now,"RFID")
	cur.execute(sql_string)
	con.commit()

def insert_AlcoholFree():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Alcohol Free","-330",now,"RFID")
	cur.execute(sql_string)
	con.commit()
	
def insert_FarmPressedMediumCider():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Farm Pressed Medium Cider","-500",now,"RFID")
	cur.execute(sql_string)
	con.commit()
	
def insert_2011VintageCider():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("2011 Vintage Cider","-500",now,"RFID")
	cur.execute(sql_string)
	con.commit()
	
def insert_Crabbies():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Crabbies","-500",now,"RFID")
	cur.execute(sql_string)
	con.commit()
	
def insert_VintageReserve():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Vintage Reserve","-568",now,"RFID")
	cur.execute(sql_string)
	con.commit()
	
def insert_MochaBeer():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Mocha Beer","-568",now,"RFID")
	cur.execute(sql_string)
	con.commit()
	
def insert_Pumpking():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Pumpking","-568",now,"RFID")
	cur.execute(sql_string)
	con.commit()
	
def insert_Rudolph():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Rudolph","-568",now,"RFID")
	cur.execute(sql_string)
	con.commit()
	
def insert_BlackCherryCider():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Black Cherry Cider","-568",now,"RFID")
	cur.execute(sql_string)
	con.commit()
	
def insert_GingerZest():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Ginger Zest","-330",now,"RFID")
	cur.execute(sql_string)
	con.commit()

def insert_PeachandApricotCider():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Peach & Apricot Cider","-500",now,"RFID")
	cur.execute(sql_string)
	con.commit()

def insert_Magners():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Magners","-440",now,"RFID")
	cur.execute(sql_string)
	con.commit()

def insert_Corona():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Corona","-330",now,"RFID")
	cur.execute(sql_string)
	con.commit()

def insert_CoronaLight():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Corona Light","-330",now,"RFID")
	cur.execute(sql_string)
	con.commit()

def insert_Fosters():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Fosters","-440",now,"RFID")
	cur.execute(sql_string)
	con.commit()

def insert_Spindrift():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Spindrift","-330",now,"RFID")
	cur.execute(sql_string)
	con.commit()

def insert_CarlingCider():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Carling Cider","-500",now,"RFID")
	cur.execute(sql_string)
	con.commit()	

def insert_StrawberryandLimeCider():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Strawberry and Lime Cider","-500",now,"RFID")
	cur.execute(sql_string)
	con.commit()

def insert_PearCider():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Pear Cider","-500",now,"RFID")
	cur.execute(sql_string)
	con.commit()

def insert_NakedAppleCider():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Naked Apple Cider","-500",now,"RFID")
	cur.execute(sql_string)
	con.commit()	

def insert_BlueberryCider():
	now = datetime.datetime.now()
	con=MySQLdb.connect(user="root",passwd="raspberry",db="beer")
	cur = con.cursor()
	sql_string = "INSERT INTO BeerStock (Beer, Quantity, Date, Reason) VALUES ('%s', '%s', '%s', '%s')" % ("Blueberry Cider","-500",now,"RFID")
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
		insert_WinterZest()
		os.system("mpg321 beep-7.mp3")
		print("Winter Zest Updated")
	elif mes == '2671' :
		insert_Carlsberg()
		os.system("mpg321 beep-7.mp3")
		print("Carlsberg Updated")
	elif mes == '7515' :
		insert_Stella()
		os.system("mpg321 beep-7.mp3")
		print("Stella Updated")
	elif mes == '2560' :
		insert_SoleStar()
		os.system("mpg321 beep-7.mp3")
		print("Sole Star Updated")
	elif mes == '7235' :
		insert_SummerZest()
		os.system("mpg321 beep-7.mp3")
		print("Summer Zest Updated")
	elif mes == '3502' :
		insert_VintageReserve()
		os.system("mpg321 beep-7.mp3")
		print("Vintage Reserve Updated")
	elif mes == '9100' :
		insert_PeachandApricotCider()
		os.system("mpg321 beep-7.mp3")
		print("Peach and Apricot Cider Updated")
	elif mes == '6294' :
		insert_GingerZest()
		os.system("mpg321 beep-7.mp3")
		print("Ginger Zest Updated")
	elif mes == '9833' :
		insert_Magners()
		os.system("mpg321 beep-7.mp3")
		print("Magners Updated")
	elif mes == '2408' :
		insert_Corona()
		os.system("mpg321 beep-7.mp3")
		print("Corona Updated")
	elif mes == '2543' :
		insert_Fosters()
		os.system("mpg321 beep-7.mp3")
		print("Fosters Updated")
	elif mes == '7196' :
		insert_Spindrift()
		os.system("mpg321 beep-7.mp3")
		print("Spindrift Updated")
	elif mes == '3751' :
		insert_CarlingCider()
		os.system("mpg321 beep-7.mp3")
		print("Carling Cider Updated")
	elif mes == '5666' :
		insert_BittersweetAppleCider()
		os.system("mpg321 beep-7.mp3")
		print("Bittersweet Apple Cider Cider Updated")
	elif mes == '6341' :
		insert_OriginalAppleCider()
		os.system("mpg321 beep-7.mp3")
		print("Original Apple Cider Updated")
	elif mes == '7229' :
		insert_TuttiFruttiPearCider()
		os.system("mpg321 beep-7.mp3")
		print("Tutti Frutti Cider Updated")
	elif mes == '5162' :
		insert_StrawberryCider()
		os.system("mpg321 beep-7.mp3")
		print("Strawberry Cider Updated")
	elif mes == '8887' :
		insert_CoronaLight()
		os.system("mpg321 beep-7.mp3")
		print("Corona Light Updated")
	elif mes == '2569' :
		insert_StrawberryandLimeCider()
		os.system("mpg321 beep-7.mp3")
		print("Strawberry and Lime Updated")
	elif mes == '5779' :
		insert_PearCider()
		os.system("mpg321 beep-7.mp3")
		print("Pear Cider Updated")
	elif mes == '6199' :
		insert_NakedAppleCider()
		os.system("mpg321 beep-7.mp3")
		print("Naked Apple Cider Updated")
	elif mes == '2832' :
		insert_BlueberryCider()
		os.system("mpg321 beep-7.mp3")
		print("Blueberry Cider Updated")
	else:
		time.sleep(0.5)
	time.sleep(0.5)

