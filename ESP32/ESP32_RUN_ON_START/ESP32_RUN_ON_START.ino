#include <WiFi.h>
void setup() {
    Serial.begin(115200);
    WiFi.mode(WIFI_STA);
    Serial.println("Make sure to input each of the ESP32's Mac macAddress in the code, included MAC is for my personal use:")
    Serial.print("MAC ADDRESS: ")
    Serial.println(WiFi.macAddress());
}
void loop() {/*leave empty pwease :3*/}
