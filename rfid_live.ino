/*RFID Shield Example Code
This code was written to work with the RFID Shield from Rob Goddard Designs www.RGDesigns.co.uk

I have adapted it to give just the Serial Number - andy@hymaswood.co.uk
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
         Serial.print(serialNumber);
         Serial.print("\n");
      reader = 0;
      readCount = 0;
  }
} 

