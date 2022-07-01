#include <Servo.h>

Servo ser_x;
Servo ser_y;

String serial_data;

void setup() {
  ser_x.attach(10);
  ser_y.attach(11);
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
}

void serialEvent() {
  serial_data = Serial.readString();
  Serial.println(serial_data);
  ser_x.write(parse_data_x(serial_data));
  ser_y.write(parse_data_y(serial_data));
}

int parse_data_x(String data) {
  data.remove(data.indexOf("Y"));
  data.remove(data.indexOf("X"), 1);
  return data.toInt();
}

int parse_data_y(String data) {
  data.remove(0, data.indexOf("Y") + 1);
  return data.toInt();
}
