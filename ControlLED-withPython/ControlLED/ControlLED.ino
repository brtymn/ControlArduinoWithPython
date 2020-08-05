#include <SerialCommand.h>

#define arduinoRED 9
SerialCommand SCmd;

void setup()
{
  pinMode(arduinoRED, OUTPUT);
  digitalWrite(arduinoRED, LOW);
  Serial.begin(9600);
  SCmd.addCommand("LEDON", RED_on);
  SCmd.addCommand("OFF", LED_off);
  SCmd.addCommand("LEDPWM", process_red);
  Serial.println("Ready");
}

void loop()
{
  SCmd.readSerial();
}


void LED_on() {
  Serial.println("LED on");
  digitalWrite(arduinoLED, HIGH);
}
void LED_off()
{
  Serial.println("LED off");
  digitalWrite(arduinoLED, LOW);
}
void process_LED()
{
  int aNumber;
  char *arg;

  Serial.println("We're in process_command");
  arg = SCmd.next();
  if (arg != NULL)
  {
    aNumber = atoi(arg);  // Converts a char string to an integer
    analogWrite(arduinoLED, aNumber);

    Serial.print("LED Brightness: ");
    Serial.println(aNumber);
  }
}
