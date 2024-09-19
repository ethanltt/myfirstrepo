const int LED_PIN = 2;
const int BUTTON_PIN = 12;
// the setup function runs once when you press reset or power the board
void setup(){
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  Serial.begin(9600);
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_PIN, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  int buttonState = digitalRead(BUTTON_PIN); 
  Serial.print("BUTTONSTATE: ");
  Serial.println(buttonState);
 // digitalWrite(LED_PIN, HIGH);  // turn the LED on (HIGH is the voltage level)
 // delay(100);                      // wait for a second
  
  if (buttonState == LOW){
	digitalWrite(LED_PIN, HIGH);
  } else {
    digitalWrite(LED_PIN, LOW);
  }
  delay(100);                   
}
