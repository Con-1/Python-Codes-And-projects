#include <LiquidCrystal.h>
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
int ir1,ir2;
int counter=0;
int count=0;
void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("Automatic Switch..");
  lcd.setCursor(0, 1);
  delay(1000);
  lcd.print("Initiated..");
  delay(1000);
  Serial.begin(9600);
  pinMode(7,INPUT);
  pinMode(8,INPUT);
  pinMode(9,OUTPUT);
  Serial.println("Started"); 
}

void loop() {
  // set the cursor to column 0, line 1
  // (note: line 1 is the second row, since counting begins with 0):
  lcd.begin(16, 2);
  lcd.setCursor(0, 0);
  lcd.print("Count = ");
  lcd.print(counter);
  lcd.setCursor(0, 1);
  // print the number of seconds since reset:
  lcd.print("----------------");
  count++;
  Serial.println("Program Counter = ");
  Serial.print(count);
  for(;;)
  {
    ir1=digitalRead(7);
    ir2=digitalRead(8);
    if(ir1==LOW&&ir2==LOW)
      break;
  }
  for(;;)
  {
    ir1=digitalRead(7);
    ir2=digitalRead(8);
    if(ir1==HIGH||ir2==HIGH)
      break;
  }
  ir1=digitalRead(7);
  ir2=digitalRead(8);
  if(ir1==HIGH)
   {
    for(int i=0;i<150;i++)
    {
      Serial.println(i);
      ir2=digitalRead(8);
      if(ir2==HIGH)
      {
        Serial.println("Entered");
        counter++;
        lcd.setCursor(0, 1);
        lcd.print("Entered..");
        delay(500);
        Serial.println(counter);
        break;  
      }
      Serial.println("Not Entered");
    }
   }
   else if(ir2==HIGH)
   {
    for(int i=0;i<150;i++)
    {
      Serial.println(i);
      ir1=digitalRead(7);
      if(ir1==HIGH)
      {
        Serial.println("Exited");
        counter--;
        lcd.setCursor(0, 1);
        lcd.print("Exited..");
        delay(500);
        Serial.println(counter);
        break;
      }
      Serial.println("Not Exited");
    }
   }
   if(counter>=1)
   {
    digitalWrite(9,HIGH);
    Serial.println("RElay Closed");
   }
   else
   {
    digitalWrite(9,LOW);
    Serial.println("Relay Open");
    counter=0;
   }
   Serial.println("Final Counter = ");
   Serial.println(counter);
}
 

