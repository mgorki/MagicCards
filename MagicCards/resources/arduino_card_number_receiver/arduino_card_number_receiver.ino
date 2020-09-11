// For receiving the input (used to define the card in the Magic Cards experiment) from a 4x4 Matrix sent by another Arduino (using 433MHz RF module).
// Receiver

// Include RadioHead Amplitude Shift Keying Library
#include <RH_ASK.h>
// Include dependant SPI Library 
#include <SPI.h> 
 
// Create Amplitude Shift Keying Object
RH_ASK rf_driver;

// For Testing with buttons
const int pinButtonRight = 2;
const int pinButtonLeft = 3;

void setup()
{
    // For testing with buttons
    pinMode(pinButtonRight, INPUT);
    pinMode(pinButtonLeft, INPUT);
      
    // Initialize ASK Object
    rf_driver.init();
    // Setup Serial Monitor
    Serial.begin(9600);
}
 
void loop()
{
    // Set buffer to size of expected message
    uint8_t buf[2];
    uint8_t buflen = sizeof(buf);
    // Check if received packet is correct size
    if (rf_driver.recv(buf, &buflen))
    {  
      // Message received
      Serial.println((char*)buf);         
    }

    // For testing with buttons
    int stateButtonRight = digitalRead(pinButtonRight);
    int stateButtonLeft = digitalRead(pinButtonLeft);
    if(stateButtonRight == 1) 
      {
      Serial.println("r"); 
      } 
    if(stateButtonLeft == 1) 
      {
      Serial.println("l"); 
      } 
}
