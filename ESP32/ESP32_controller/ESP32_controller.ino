#include <esp_now.h>
#include <WiFi.h>

// 1. Define the MAC address of the OTHER board
uint8_t peerAddress[] = {0x24, 0x0A, 0xC4, 0x04, 0xF4, 0x40};  //Change according to the {ESP32_RUN_ON_START.ino} results

// 2. Define data structures for outgoing and incoming data
typedef struct {
    int id;
    float value;
} MessageData;

MessageData outgoingData;
MessageData incomingData;

// 3. Send Callback (Confirms delivery)
void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
    Serial.print("Sent Status: ");
    Serial.println(status == ESP_NOW_SEND_SUCCESS ? "Success" : "Fail");
}

// 4. Receive Callback (Handles incoming data instantly)
void OnDataRecv(const uint8_t *mac, const uint8_t *incomingData, int len) {
    memcpy(&incomingData, incomingData, sizeof(incomingData));
    Serial.print("Received ID: ");
    Serial.println(incomingData.id);
}

void setup() {
    Serial.begin(115200);
    WiFi.mode(WIFI_STA);

    // Initialize ESP-NOW
    if (esp_now_init() != ESP_OK) {
        Serial.println("Error initializing ESP-NOW");
        return;
    }

    // Register BOTH callbacks on THIS board
    esp_now_register_send_cb(OnDataSent);
    esp_now_register_recv_cb(OnDataRecv);

    // Add the other board as a peer
    esp_now_peer_info_t peerInfo;
    memcpy(peerInfo.peer_addr, peerAddress, 6);
    peerInfo.channel = 0;
    peerInfo.encrypt = false;

    if (esp_now_add_peer(&peerInfo) != ESP_OK) {
        Serial.println("Failed to add peer");
        return;
    }

    Serial.println("Bidirectional ESP-NOW Ready");
}

void loop() {
    // Prepare and send data independently of receiving
    outgoingData.id = 1;
    outgoingData.value = 3.14;

    esp_now_send(peerAddress, (uint8_t *) &outgoingData, sizeof(outgoingData));

    delay(1000); // Send every second, but receiving happens continuously in background
}
