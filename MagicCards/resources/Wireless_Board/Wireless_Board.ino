#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define OLED_RESET 4
Adafruit_SSD1306 display(OLED_RESET);


String html1 = {
"<form>\n"
"    <div class=\"CardNumber\">\n"
"        <label for=\"card\">Enter Card Number (1-22) or 99 to abort experiment:</label>\n"
"        <input id=\"card\" type=\"number\" name=\"card\" step=\"1\" min=\"1\" max=\"99\" required>\n"
"        <span class=\"validity\"></span>\n"
"    </div>\n"
"    <div class=\"feetInputGroup\" style=\"display: none;\">\n"
"        <span>Enter Card Number (1-22) or 99 to abort experiment</span>\n"
"        <span class=\"validity\"></span>\n"
"    </div>\n"
"    <div>\n"
"        <input type=\"submit\" value=\"Submit form\">\n"
"    </div>\n"
"</form>"
};

 
ESP8266WebServer server(80);
 
const char* ssid = "MagicCards";
const char* password =  "12345678";


void Ereignis_Index()           // Wird ausgeuehrt wenn "http://<ip address>/" aufgerufen wurde
{
      String message = "";
      //message += server.args();            //Get number of parameters
      //message += "\n";                            //Add a new line
      
      for (int i = 0; i < server.args(); i++) {
      //message += "Arg nº" + (String)i + " –> ";   //Include the current iteration value
      //message += server.argName(i) + ": ";     //Get the name of the parameter
      //message += server.arg(i) + "\n";              //Get the value of the parameter
      message += server.arg(i);
      } 

      String feedback = {"Last card sent: " + message + html1};
 
      //server.send(200, "text/plain", message);
      Serial.write("#");
      Serial.println(message);
      //delay(5000);
      server.send(200, "text/html", feedback);
}
 

 
void setup() {
 
    Serial.begin(9600);

    display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
    display.display();
    delay(1000);
    display.clearDisplay();
    
    Serial.println("Starte WLAN-Hotspot \"MagicCards\"");
    WiFi.mode(WIFI_AP);           // access point modus
    WiFi.softAP(ssid, password);    // Name des Wi-Fi netzes
    delay(5000);                   //Abwarten 5s
    Serial.print("IP Adresse ");  //Ausgabe aktueller IP des Servers
    Serial.println(WiFi.softAPIP());
 
      //  Bechandlung der Ereignissen anschlissen
    server.on("/", Ereignis_Index);
    server.on("/?card", handleCard); //Associate the handler function to the path
 
    server.begin(); //Start the server
    server.send(200, "text/html", html1);
    Serial.println("Server listening");
 
}
 
void loop() {
 
    server.handleClient(); //Handling of incoming requests
    delay(1000);
    display.setTextSize(1);
    display.setTextColor(WHITE);
    display.setCursor(0,0);
    display.println("Hallo Welt!");
    display.setCursor(0,10);
    display.println(millis());
    display.display();
    display.clearDisplay();
 
}
 
void handleCard() { //Handler for the body path
 
      String message = "Number of args received:";
      message += server.args();            //Get number of parameters
      message += "\n";                            //Add a new line
      
      for (int i = 0; i < server.args(); i++) {
      message += "Arg nº" + (String)i + " –> ";   //Include the current iteration value
      message += server.argName(i) + ": ";     //Get the name of the parameter
      message += server.arg(i) + "\n";              //Get the value of the parameter
      //message += "*" + server.arg(i) + "#";
      } 

 
      server.send(200, "text/plain", message);
      Serial.println(message);
}
