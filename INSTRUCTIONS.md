Instructions
------------------

Given time I will try and include a comprehensive screen-shotted tutorial, but for now here are some basic instructions.  Please email me if you want to be updated when the tutorial becomes available.  andy@hymaswood.co.uk You can also check out some pictures on my website http://www.hymaswood.co.uk

I have not followed these instructions through as I already have the stuff setup on my Pi, but this should work reasonably well.  Please let me know if you come across any errors or missing steps.

Install LAMP, refer to these instructions: http://elinux.org/RPi_A_Simple_Wheezy_LAMP_install

Install PHPMyAdmin, refer to these instructions (link has been removed from fusionstrike.com a new one will follow)

Install Arduino, refer to these instructions http://arduino.cc/en/Guide/HomePage 


If you want to run the Pi without a screen attached (like I did on the most part), also look at these:

Use Putty to SSH into your Pi, refer to these instructions http://elinux.org/RPi_A_Method_for_ssh_blind_login 

Install VNCServer, refer to these instructions http://elinux.org/RPi_Wheezy_VNC 



Using PHPMyAdmin or the MySQL Command Line Interface, setup the database "beer" and load the information by loading the sql scripts.  This will setup a new database and the data tables for you as well as some dummy data.  Refer to the instructions provided by each application on how to do this.  Once loaded, you can adjust the Beer information and BeerStock information if you wish, or just leave it as is for testing.


Use the fritzing diagram here https://github.com/anddav87/SendTempWarn/blob/master/Temp%20Sensor_bb.png  to setup your DS18B20 temperature sensor on the breadboard, and attach it to the Pi’s GPIO ports.  You could test this setup first separately using this code https://github.com/anddav87/SendTempWarn 


I managed to purchase an RFID reader for £15 from http://www.rgdesigns.co.uk so my code is all based on this.  You will have to change how this works if you are using a different RFID reader e.g. the Parallax reader but as long as it can report the tag to a Serial port, you shouldn’t have an issue.  Solder the RFID reader together and attach it to your Arduino.  Load the test Arduino Sketch (the default one that is provided by rgdesigns.co.uk) and check the Serial Monitor to check it is working ok.  Load the live Arduino Sketch and check the Serial Monitor to check the Tag is being read ok.  Keep a note of the tag numbers and what Beers you will be associating to them.


Install pyserial from here http://pyserial.sourceforge.net/ 


Change the sqlrfidbeerstock1.py script to reference the tag numbers you have to a couple of the beers.


Load the keg folder into the /var/www folder of your Pi (can do this by FTP, as long as you are logged in as root or use the sudo command to copy from your /home/pi folder assuming the structure is this /home/pi/keg you would use this command sudo cp –r /home/pi/keg /var/www/keg)


Run the temperature script and RFID script on the Pi (if working remotely run these from Putty or if you want to be able to disconnect from the Pi and leave it running, try using VNC.  I hear lots of good things about using “screen” but haven’t tried it yet)


Access the PHP file from the Pi’s browser or another computer/device on the same network e.g. http://192.168.0.14/keg/beer.php if your IP address is 192.168.0.14 or if you are clever you can change your hostname of the Pi and access it like http://raspberrypi/keg/beer.php (but you will need to refer to separate instructions on changing your hostname).  You should see the latest recorded temperature and all the beer info.  Swipe a tag across the RFID reader, wait for the beep and watch the stock level adjust when the page is refreshed.


Tweaks you can play with:

a) Change the sound played when a tag is read.  I like the idea of a Star Trek computer sound or as that is too geeky for a BBQ with friends, maybe Homer Simpson?

b) Change the sound to be different for each beer

c) Play an error sound if a tag is read that is not in the database

d) Assign a tag to an increase in stock level for a standard crate of beer e.g. 12 * 330ml to simplify updating for new purchases

e) Get the browser to refresh the page every minute or x minutes depending on big your party is.  


Future Development Ideas:

a) Depending on the Tag ID’s, maybe implement joining the site code and ID together as a unique number instead

b) Use RFID stickers rather than tags, to actually stick to the bottles (could be expensive!)

c) Store the tag information in a database table rather than the python script and change the trigger accordingly

d) Change the background or make a lower res one that is quicker to load

e)Add a purple SRM for Fruit Ciders


Credits

a) Beer Labelizer: http://www.beerlabelizer.com

b) Kegerface Original: https://github.com/Kegerface/Kegerface

c) O’Reilly Learning PHP, MySQL and JavaScript: http://www.amazon.co.uk/Learning-MySQL-JavaScript-Step---Step/dp/1449319262/ref=sr_1_1?ie=UTF8&qid=1366891307&sr=8-1&keywords=learning+php+mysql+and+javascript

d) Adafruit Temperautre Sensor Tutorial: http://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing

e) Adafruit Serial PIR Tutorial: http://learn.adafruit.com/arduino-lesson-17-email-sending-movement-detector

f)RG Designs RFID Arduino Code: http://www.rgdesigns.co.uk
