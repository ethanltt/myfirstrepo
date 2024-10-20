#include <Servo.h>

Servo myServo;
Servo myServo2;

const int LED_PIN = 11;
const int BUTTON_PIN = 12;
const int BUTTON_PIN2 = 10;
const int SERVO_PIN=4;
const int SERVO_PIN2=5;

// the setup function runs once when you press reset or power the board
void setup(){
  pinMode(BUTTON_PIN,INPUT_PULLUP);
  pinMode(BUTTON_PIN2,INPUT_PULLUP);

  Serial.begin(9600);
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_PIN, OUTPUT);
  
  myServo.attach(SERVO_PIN);
  myServo2.attach(SERVO_PIN2);
  
  myServo.write(0);
  myServo2.write(0);
}

// the loop function runs over and over again forever
void loop() {
  int buttonState = digitalRead(BUTTON_PIN); 
  int buttonState2 = digitalRead(BUTTON_PIN2); 
  Serial.print("BUTTONSTATE: ");
  Serial.println(buttonState);

  Serial.print("BUTTONSTATE2: ");
  Serial.println(buttonState2);
  
  if (buttonState2 == LOW) {
  	digitalWrite(LED_PIN, HIGH);
    myServo2.write(90);
  } else {
    digitalWrite(LED_PIN, LOW);
    myServo2.write(0);
  }

  if (buttonState == LOW) {
  	digitalWrite(LED_PIN, HIGH);
    myServo.write(180);
  } else {
    digitalWrite(LED_PIN, LOW);
    myServo.write(0);
  }

  
   
  delay(200);                   
}
