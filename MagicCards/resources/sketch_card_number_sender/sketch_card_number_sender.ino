#include <Keypad.h>

//// Include RadioHead Amplitude Shift Keying Library
//#include <RH_ASK.h>
//// Include dependant SPI Library 
//#include <SPI.h> 

// include the LiquidCrystal library for use of the LCD-screen:
#include <LiquidCrystal.h>

//// Create Amplitude Shift Keying Object
//RH_ASK rf_driver;

// initialize the LiquidCrystal library with the numbers of the interface pins
LiquidCrystal lcd(A0, A1, A2, A3, A4, A5);

const int ROW_NUM = 4; //four rows
const int COLUMN_NUM = 3; //three columns

char keys[ROW_NUM][COLUMN_NUM] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};

byte pin_rows[ROW_NUM] = {9, 8, 7, 6}; //connect to the row pinouts of the keypad
byte pin_column[COLUMN_NUM] = {5, 4, 3}; //connect to the column pinouts of the keypad

Keypad keypad = Keypad( makeKeymap(keys), pin_rows, pin_column, ROW_NUM, COLUMN_NUM );

String card_number;

void setup(){
  Serial.begin(9600);
  card_number.reserve(3); // maximum input characters is 2 (plus NULL character), change if needed
//  rf_driver.init(); // Initialize ASK Object

  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);

  // presenting LCD's startup message ( = basic instructions) for 10 seconds
  lcd.clear();
  lcd.print("# = confirm");
  lcd.setCursor(0, 1);
  lcd.print("* = correction");
  delay(10000);
  lcd.clear();
  lcd.setCursor(0, 0);  
}

void loop(){
  char key = keypad.getKey();
  
  if (key){
    // Confirming (= sending) the current number   
    if(key == '#') {
      if (card_number.length() == 2) {
        const char *msg = card_number.c_str();
        //rf_driver.send((uint8_t *)msg, strlen(msg));
        //rf_driver.waitPacketSent();
        Serial.println(msg);
        lcd.print(" sent");
        delay(1000);
        card_number = "";
        
        //Empty the display
        lcd.clear();
      }
      else {
      lcd.clear();
      card_number = "";
      lcd.print("enter 2 digits!");
      delay(1500);
      lcd.clear();  
      }
    }

    // Correcting the current number
    else if (key == '*') {  
      card_number = "";
      lcd.clear();
      lcd.print(card_number); // For testing only
      lcd.print("enter again");
      delay(1500);
      lcd.clear();
    }

    // Appending another digit to the current number
    else {
      card_number += key; // append new character to input password string
      delay(200); // In order to avoid pressing the same digit acidentally two times
      lcd.print(key); // Print the current number to the LCD.
    }
  }
}
