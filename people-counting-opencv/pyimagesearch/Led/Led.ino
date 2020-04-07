int data;
int LEDRed=13;
int LEDGreen=15;
void setup() 
{ 
  Serial.begin(9600); //initialize serial COM at 9600 baudrate
  pinMode(LEDGreen, OUTPUT); //declare the LED pin (15) as output
  digitalWrite (LEDGreen, LOW); //initially set to low
  pinMode(LEDRed, OUTPUT); //declare the LED pin (13) as output
  digitalWrite (LEDRed, LOW); //initially set to low
  Serial.println("This is my First Example."); //Turn OFF the LedGreen in the beginning
}
 
void loop() 
{
while (Serial.available()) //whatever the data that is coming in serially and assigning the value to the variable “data”
  {
    data = Serial.read();
  }

  if (data == '0')
  digitalWrite (LEDRed, HIGH);
  digitalWrite (LEDGreen, LOW);

  else if (data == '1')
  digitalWrite (LEDRed, LOW);
  digitalWrite (LEDGreen, HIGH);

}
