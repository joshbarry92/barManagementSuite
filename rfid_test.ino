/*RFID Shield Example Code
This code is written to work with the RFID Shield from Rob Goddard Designs
This example is simply designed to read the serial number and site ID and
send it to the computer.

WWW.RGDesigns.co.uk
*/

long reader = 0;
int readCount = 0;


void readOne(void) 
{
  readCount++;
  reader = reader << 1;
  reader |= 1;
}

void readZero(void) 
{
  readCount++;
  reader = reader << 1;
}

void setup()
{
  Serial.begin(115200);
  attachInterrupt(0, readZero, RISING);
  attachInterrupt(1, readOne, RISING);
  delay(10);
  for(int i = 2; i<4; i++)
  {
    pinMode(i, OUTPUT);
    digitalWrite(i, HIGH); // enable internal pull up causing a one
    digitalWrite(i, LOW); // disable internal pull up causing zero and thus an interrupt
    pinMode(i, INPUT);
    digitalWrite(i, HIGH); // enable internal pull up
  }
  
 // delay(10);
  reader = 0;
  readCount = 0;
}

void loop() {
 if(readCount >=26){
   int serialNumber=(reader >> 1) & 0x3fff;
   int siteCode= (reader >> 17) & 0x3ff;
         Serial.print("RFID Detected\n");
         Serial.print("=============\n");
         Serial.print("Serial Number = ");
         Serial.print(serialNumber);
         Serial.print("\n");
         Serial.print("Site Code = ");
         Serial.print(siteCode);         
         Serial.print("\n\n");
      reader = 0;
      readCount = 0;
  }
} 
