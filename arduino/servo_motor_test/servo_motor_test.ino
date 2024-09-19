#include <Servo.h>

Servo myServo;

const int LED_PIN = 14;
const int BUTTON_PIN = 12;
const int SERVO_PIN=4;

// the setup function runs once when you press reset or power the board
void setup(){
  pinMode(BUTTON_PIN,INPUT_PULLUP);
  Serial.begin(9600);
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_PIN, OUTPUT);
  
  myServo.attach(SERVO_PIN);
  myServo.write(0);
}

// the loop function runs over and over again forever
void loop() {
  int buttonState = digitalRead(BUTTON_PIN); 
  Serial.print("BUTTONSTATE: ");
  Serial.println(buttonState);
  
  if (buttonState == LOW) {
  	digitalWrite(LED_PIN, HIGH);
    myServo.write(180);
  } else {
    digitalWrite(LED_PIN, LOW);
    myServo.write(0);
  }
   
  delay(200);                   
}
