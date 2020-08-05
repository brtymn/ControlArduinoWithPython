 
#include <SerialCommand.h>                    
#define pwmA 9                                
#define pwmB 10                               
SerialCommand SCmd;                           
void setup() {
  pinMode(pwmA, OUTPUT);                      
  pinMode(pwmB, OUTPUT);                      
  Serial.begin(9600);                         
  SCmd.addCommand("PWM", pwm);                
  SCmd.addDefaultHandler(unrecognized);       
  Serial.println("Ready");}                   
void loop() {  SCmd.readSerial();}            
void pwm() {                                  
  int aNumber;                                
  int bNumber;                                
  char *arg;                                  
  char *arg2;                                 
  Serial.println("We're in process_command"); 
  arg = SCmd.next();                          
  if (arg != NULL)                            
  { aNumber = atoi(arg);                      
    analogWrite(pwmA, aNumber);               
    Serial.print("First argument was: ");     
    Serial.println(aNumber);  }               
  else {                                      
    Serial.println("No arguments");  }        
  arg2 = SCmd.next();                        
  if (arg2 != NULL)                           
  { bNumber = atol(arg2);                    
    analogWrite(pwmB, bNumber);               
    Serial.print("Second argument was: ");    
    Serial.println(bNumber);  }               
  else {                                      
    Serial.println("No second argument");  }  
}
void unrecognized() {                         
  Serial.println("What?");}  
