// Fan Pinout
int fanSens = 2; // Fan sens (tach) wire connected to digital_2 port
int PWMpin  = 3; // Fan PWM wire connected to digital_3 port

// Temperature Pinout
// int tempPin = A5; // Middle pin of LM35 connected to analog_A1 port

// Internal variables 
unsigned long pulseDuration;
char incomingByte;
unsigned int integerValue = 0;

void setup() {
  analogWrite(PWMpin, 90);
  Serial.println("starting...");
  pinMode(fanSens, INPUT);
  Serial.begin(9600);
}

//---------------------- Show & Control RPM -----------------------------//
void showRPM() {
  pulseDuration = pulseIn(fanSens, LOW);
  double frequency = 1000000 / pulseDuration / 2 * 60 / 2;
  Serial.println(frequency);
}

void setRPM(int analogValue) {
  if (analogValue > 100 && analogValue < 256) {
    analogWrite(PWMpin, analogValue);
  }
}

//--------------------- Compute RPM from Serial Input ------------------//

int getAnalogMap(int digit) {
  int writeMap[10] = {110,128,146,164,190,208,226,237,242,255};
  return writeMap[digit];
}

int computeInput(int input) {
  int analogVal = getAnalogMap(input);
  setRPM(analogVal);
}

//--------------------- Main Loop --------------------------------------//

void loop() {
   while (Serial.available() > 0) {
    incomingByte = Serial.read()- '0'; // read the incoming byte:
    computeInput(incomingByte);
  }
  showRPM();
}
