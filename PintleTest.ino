// Pintle Sensor reader script. Prints data over serial for interpretatino using other script


// Global modifiers and input parameters

const int rangeXDucer[] = {5000, 3000, 4000}; // Upper range of tranducers in PSI
const int numXDucer = 3;
const int analogResolution = 1024; //Arduino native analog input resolution

// Set analog pin numbers

const int pinXDucer[] = {0,1,2};          // Will use pins 0-2
const int pinFlowMeter = (numXDucer + 1); // Will be the highest numbered analog pin

// Variable for data read in

//int pressureXDucer[] = {0};
int flowMeter = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
	for(int i = 0; i < numXDucer; i++){
		Serial.print(analogRead((pinXDucer[i] * rangeXDucer[i] / analogResolution)));
   delay(0);
		Serial.write(',');
	}
	Serial.print(analogRead(pinFlowMeter));
	Serial.print('\n');
  delay(0.1);
}
