char data = 0;
int led = 13;
void setup() {
    Serial1.begin(9600);
    pinMode(led, OUTPUT);
}
void loop() {
    Serial1.write("5");
    while(Serial1.available() > 0){
        data = Serial1.read();
        if(data == 1){
            digitalWrite(led, HIGH);
            delay(3000);
            digitalWrite(led, LOW);
        }
    }
}