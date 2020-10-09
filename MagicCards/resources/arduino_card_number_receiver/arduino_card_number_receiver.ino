// For receiving the input (used to define the card in the Magic Cards experiment) from a 4x4 Matrix sent by another Arduino (using 433MHz RF module).
// Receiver
//
//// Include RadioHead Amplitude Shift Keying Library
//#include <RH_ASK.h>
//// Include dependant SPI Library 
//#include <SPI.h> 

//// Create Amplitude Shift Keying Object
//RH_ASK rf_driver;

const byte numChars = 32;
char msg[numChars]; // an array to store the received data
byte button_msg[2]; // an array for sending the button states to the pc 

boolean newNumber = false;

// For the buttons
const int pinButtonRight = 2;
const int pinButtonLeft = 4;

void setup()
{
    // For testing with buttons
    pinMode(pinButtonRight, INPUT);
    pinMode(pinButtonLeft, INPUT);
//      
//    // Initialize ASK Object
//    rf_driver.init();
    // Setup Serial Monitor
    Serial.begin(38400);
}
 
void loop()
{
//    // Set buffer to size of expected message
//    uint8_t buf[2];
//    uint8_t buflen = sizeof(buf);
//    // Check if received packet is correct size
//    if (rf_driver.recv(buf, &buflen))
//    {  
//      // Message received
//      Serial.println((char*)buf);         
//    }

    RecvEndMarkerNewline();
    passNumber();
    newNumber = false;
    
    // For the buttons
    int stateButtonRight = digitalRead(pinButtonRight);
    int stateButtonLeft = digitalRead(pinButtonLeft);

    button_msg[0] = 0x30;
    button_msg[1] = 0x30; 
      
    if(stateButtonRight == 1) 
      {
      button_msg[0] = 0x31;
      }
    if(stateButtonLeft == 1) 
      {
      button_msg[1] = 0x31;
      }

    Serial.write("*"); 
    Serial.write(button_msg, 2);

}

void RecvEndMarkerNewline() {
   static byte ndx = 0;
   char endMarker = '\n';
   char rc;
   
   // if (Serial.available() > 0) {
   while (Serial.available() > 0 && newNumber == false) {
   rc = Serial.read();
  
   if (rc != endMarker) 
   {
   msg[ndx] = rc;
   ndx++;
     if (ndx >= numChars) 
     {
      ndx = numChars - 1;
     }
   }
   else {
     msg[ndx] = '\0'; // terminate the string
     ndx = 0;
     newNumber = true;
   }
   }
}

void passNumber() {
 if (newNumber == true) 
 {
   Serial.write("#");
   Serial.println(msg);
   delay(100);
   newNumber = false;
 }
}
