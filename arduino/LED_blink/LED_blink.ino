// Define the pin number where the LED is connected
const int ledPin = 5;

void setup() {
  // Set the LED pin as an output
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Turn the LED on by setting the pin HIGH
  digitalWrite(ledPin, HIGH);
  
  // Wait for 5 seconds (5000 milliseconds)
  delay(25);
  
  // Turn the LED off by setting the pin LOW
  digitalWrite(ledPin, LOW);
  
  // Wait for another 5 seconds before repeating the loop
  delay(25);
}


