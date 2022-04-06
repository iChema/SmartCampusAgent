// Example testing sketch for various DHT humidity/temperature sensors written by ladyada
// REQUIRES the following Arduino libraries:
// - DHT Sensor Library: https://github.com/adafruit/DHT-sensor-library
// - Adafruit Unified Sensor Lib: https://github.com/adafruit/Adafruit_Sensor

#include <RBDdimmer.h>//https://github.com/RobotDynOfficial/RBDDimmer
#include "DHT.h"
//#define LED 2
#define SENSOR1 4
#define SENSOR2 34
#define SOUND 35
#define DELAY 500

#define DHTPIN 5     // Digital pin connected to the DHT sensor
// Feather HUZZAH ESP8266 note: use pins 3, 4, 5, 12, 13 or 14 --
// Pin 15 can work but DHT must be disconnected during program upload.

// Uncomment whatever type you're using!
#define DHTTYPE DHT11   // DHT 11
//#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321
//#define DHTTYPE DHT21   // DHT 21 (AM2301)

// Connect pin 1 (on the left) of the sensor to +5V
// NOTE: If using a board with 3.3V logic like an Arduino Due connect pin 1
// to 3.3V instead of 5V!
// Connect pin 2 of the sensor to whatever your DHTPIN is
// Connect pin 4 (on the right) of the sensor to GROUND
// Connect a 10K resistor from pin 2 (data) to pin 1 (power) of the sensor

// Initialize DHT sensor.
// Note that older versions of this library took an optional third parameter to
// tweak the timings for faster processors.  This parameter is no longer needed
// as the current DHT reading algorithm adjusts itself to work on faster procs.
DHT dht(DHTPIN, DHTTYPE);

const int zeroCrossPin  = 18;
const int acdPin  = 19;
int CO2SensorValue = 0;  // variable to store the value coming from the sensor
int COSensorValue = 0;  // variable to store the value coming from the sensor
int SoundSensorValue = 0;  // variable to store the value coming from the sensor
float h = 0;
float t = 0;
float f = 0;
float hif = 0;
float hic = 0;
uint8_t idx = 0;
char c;
char str[255];

//Objects
dimmerLamp acd(acdPin, zeroCrossPin);

void setup() {
  //pinMode(LED, OUTPUT);
  Serial.begin(115200);
  //Serial.println("Sensor start");
  //Serial.println(F("DHTxx test!"));
  dht.begin();
  acd.begin(NORMAL_MODE, ON);
}

void loop() {
  if (Serial.available() > 0) {
    c = Serial.read();
    if (c != '\n') {
      str[idx++] = c;
    }
    else {
      str[idx++] = '\0';
      idx = 0;
      //Serial.print("Datos: ");
      //digitalWrite(LED, HIGH);   // turn the LED on (HIGH is the voltage level)
      // delay(DELAY);              // wait for a second
      // Wait a few seconds between measurements.
      if (String(str).equals("SENSORS")) {
        // read the value from the sensor:
        CO2SensorValue = analogRead(SENSOR1);
        //Serial.print("Value CO2: "); Serial.println(CO2SensorValue);
        COSensorValue = analogRead(SENSOR2);
        //Serial.print("Value CO: "); Serial.println(COSensorValue);
        SoundSensorValue = analogRead(SOUND);
        //Serial.print("Value sound: "); Serial.println(SoundSensorValue);
        //digitalWrite(LED, LOW);    // turn the LED off by making the voltage LOW

        // Reading temperature or humidity takes about 250 milliseconds!
        // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
        h = dht.readHumidity();
        // Read temperature as Celsius (the default)
        t = dht.readTemperature();
        // Read temperature as Fahrenheit (isFahrenheit = true)
        f = dht.readTemperature(true);

        // Check if any reads failed and exit early (to try again).
        if (isnan(h) || isnan(t) || isnan(f)) {
          //Serial.println(F("Failed to read from DHT sensor!"));
          //return;
          h = 0;
          t = 0;
          f = 0;
        }

        // Compute heat index in Fahrenheit (the default)
        hif = dht.computeHeatIndex(f, h);
        // Compute heat index in Celsius (isFahreheit = false)
        hic = dht.computeHeatIndex(t, h, false);

        Serial.print(String(CO2SensorValue) + "," + String(COSensorValue) + "," + String(SoundSensorValue) + "," + String(h) + "," + String(t) + "," + String(f) + "," + String(hic) + "," + String(hif));
      } else if (String(str).equals("OFF")) {
        acd.setState(OFF);
      } else {
        acd.setPower(String(str).toFloat());
      }

      /*
        Serial.print(F("Humidity: "));
        Serial.print(h);
        Serial.print(F("%  Temperature: "));
        Serial.print(t);
        Serial.print(F("°C "));
        Serial.print(f);
        Serial.print(F("°F  Heat index: "));
        Serial.print(hic);
        Serial.print(F("°C "));
        Serial.print(hif);
        Serial.println(F("°F"));
      */
    }
    /*
      //digitalWrite(LED, HIGH);   // turn the LED on (HIGH is the voltage level)
      delay(DELAY);              // wait for a second
      // Wait a few seconds between measurements.
      // read the value from the sensor:
      CO2SensorValue = analogRead(SENSOR1);
      //Serial.print("Value CO2: "); Serial.println(CO2SensorValue);
      COSensorValue = analogRead(SENSOR2);
      //Serial.print("Value CO: "); Serial.println(COSensorValue);
      SoundSensorValue = analogRead(SOUND);
      //Serial.print("Value sound: "); Serial.println(SoundSensorValue);

      //digitalWrite(LED, LOW);    // turn the LED off by making the voltage LOW

      // Reading temperature or humidity takes about 250 milliseconds!
      // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
      h = dht.readHumidity();
      // Read temperature as Celsius (the default)
      t = dht.readTemperature();
      // Read temperature as Fahrenheit (isFahrenheit = true)
      f = dht.readTemperature(true);

      // Check if any reads failed and exit early (to try again).
      if (isnan(h) || isnan(t) || isnan(f)) {
      //Serial.println(F("Failed to read from DHT sensor!"));
      return;
      }

      // Compute heat index in Fahrenheit (the default)
      hif = dht.computeHeatIndex(f, h);
      // Compute heat index in Celsius (isFahreheit = false)
      hic = dht.computeHeatIndex(t, h, false);

      Serial.println(String(CO2SensorValue)+","+String(COSensorValue)+","+String(SoundSensorValue)+","+String(h)+","+String(t)+","+String(f)+","+String(hic)+","+String(hif));
      Serial.print(F("Humidity: "));
      Serial.print(h);
      Serial.print(F("%  Temperature: "));
      Serial.print(t);
      Serial.print(F("°C "));
      Serial.print(f);
      Serial.print(F("°F  Heat index: "));
      Serial.print(hic);
      Serial.print(F("°C "));
      Serial.print(hif);
      Serial.println(F("°F"));
    */
  }
}
