/****************************************************************************/
int val;
int encoder0PinA = 6;
int encoder0PinB = 7;
int encoder0ButtonPin = 2;
int encoder0PosX = 0;
int encoder0PosY = 0;
int encoder0PinALast = LOW;
int n = LOW;
volatile byte flag = 1;
/****************************************************************************/
void setup() {
  pinMode (encoder0PinA, INPUT);
  pinMode (encoder0PinB, INPUT);
  attachInterrupt(digitalPinToInterrupt(encoder0ButtonPin), change, RISING);
  pinMode (encoder0ButtonPin, INPUT_PULLUP);
  Serial.begin (9600);
}
/****************************************************************************/
void loop() {
  n = digitalRead(encoder0PinA);
  if (flag == 1)
  {
    if ((encoder0PinALast == LOW) && (n == HIGH)) {
      if (digitalRead(encoder0PinB) == LOW) {
        if (encoder0PosX >= -240)
          encoder0PosX--;
      } else {
        if (encoder0PosX <= 240)
          encoder0PosX++;
      }
      Serial.println(String(flag) + String(encoder0PosX));
    }
  }
  else
  {
    if ((encoder0PinALast == LOW) && (n == HIGH)) {
      if (digitalRead(encoder0PinB) == LOW) {
        if (encoder0PosY >= -240)
          encoder0PosY--;
      } else {
        if (encoder0PosY <= 240)
          encoder0PosY++;
      }
      Serial.println(String(flag) + String(encoder0PosY));
    }
  }
  encoder0PinALast = n;
}

/****************************************************************************/
void change() {
  flag = !flag;
}
/****************************************************************************/
