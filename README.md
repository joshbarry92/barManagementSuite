Inspired by the original Kegerface project</a> I decided to make some adaptations for our home bar as a way of learning more about my Raspberry Pi and recently acquired Arduino.  I came up with a satisfactorily OTT setup.  Geekery and beer, what could be a better combination?  

Rather than list what which of our homebrew beers were "on tap" I decided to list what commercial beers we stocked in our home bar.  For this reason I should probably rename it "Barface" as opposed to "Kegerface" but I wanted to stay true to the original idea.  I had seen a similar setup in a bar in Calgary when I was working there for a short while, so wanted to mix the two ideas.
 
I also wanted a way to keep track of the actual stock we had rather than an ambiguous picture.  I wasn't happy with storing the information in a CSV file and repeating the information for each new beer record in the PHP file, I decided to store the data in MySQL and let the Kegerface display the information for all the beers using queries.  Once I had implemented that, I decided I wanted a quick and easy way to update the stock as a beer was taken from the bar.  I meddled with using phpMyAdmin to update the BeerStock table and then created a PHP form to fill out manually, but it was labour-intensive and not practical for daily use.  So, I decided to implement an RFID reader to update the stock level.  A barcode reader may have been more practical (one code per beer rather than, say, 12 possible codes if you are assigning one tag per bottle) but not nearly as OTT as I would have liked. ;)
 
I also wanted to display the current temperature at the bar.  I used a DS18B20 temperature sensor to achieve this, and later moved to a waterproof version of the sensor, that I could dangle in an ice bucket.  The temperature is logged to a MySQL table and displayed on the Kegerface.

Please be gentle with me: this was my first real go at using PHP, CSS, Python, Arduino and MySQL as well as my first real go at using Linux rather than Windows.  Because of this, and as the project grew in its complexity as I achieved more things, I probably haven't completed everything as simply as it could have been but it works for me and I am reasonably happy, to the point that I wanted to share what I have done.  Please bear this in mind before pointing out any obvious flaws!  However, any constructive comments are more than welcome.

I have summarised below the changes from the original Kegerface:

1. Put the data into an HTML table rather than rely on CSS
The original Kegerface CSS used specific values to display on the screen it was built to use, and in the different browsers I was using on my work laptop and home laptop as well as phones, tablets and so on, it would never show correctly.  The images would hover over parts of other records and I couldn’t seem to correct this, however much I manipulated the original files.  I love HTML tables (as much as some others loathe them) so decided to go this route as my CSS is worse than my SQL…

2. Change SRM images
The original SRM images with the white background looked pretty squished and not very pretty, even when taking away the white edge.  So I changed them, and also increased the number of SRM images that were available as I found that some of my ciders had a lower SRM and I wanted to show this correctly (I still need to do a purple one for the fruit ciders!)

3. Revamped the background
Because of my display width, the background was repeating, and this was obvious.  I flipped and mirrored the original image left to right and then top to bottom, so that the background could repeat without being obvious.  Unfortunately it takes a while to load.

4. Resized the images
I resized the Hop, SRM and Stock images to load faster, which was necessary when testing on the web and doing lots of refreshes from different devices.  Probably not necessary for the Raspberry Pi, but I was happier with them this way

5. Added header image
Using the Beer Labelizer website, I created a custom header image

6. Use a MySQL database instead of CSV file
There are two tables in the MySQL database, one that stores beer information and one that stores stock information.  They are linked by the beer name in my query.  There is also a separate table to hold the temperature information, if you decide to hook up a sensor.

7. Changing keg image based on actual stock value
Rather than have to adjust the "stock" value on the beer table, as our stock decreased, I built a new table to hold stock updates.  Then in my query, it refers to the sum of the stock and then hooks that up to an appropriate keg image.

8. List the remaining value
The number of available Pints is also shown for reference.  Being a decimal boy, the Stock table uses ml and rounds this to the nearest Pint for the Kegerface display.

9. Add the current temperature
The temperature is recorded using a waterproof DS18B20 sensor and logged into MySQL.  The information can be queried from the Kegerface PHP file.

10. Simplify Stock Update using RFID
I attached an RFID reader to my Arduino and hooked this up to the Pi.  There is a python script that runs on the Pi, and “reads” the tags from the RFID reader using the serial port, and adds a record into the BeerStock table accordingly.  Note that I used a powered USB hub to power the Arduino, I am not sure how that would run attached straight to the Pi.
