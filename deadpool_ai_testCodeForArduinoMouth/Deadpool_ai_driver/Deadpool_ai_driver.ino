#include <Servo.h>

class TalkingMouth {
private:
  Servo mouth;

public:
  TalkingMouth() {}

  void initialize() {
    Serial.begin(9600);
    mouth.attach(9);
    mouth.write(50);  // Set the initial position
  }

  void moveMouth(int position, int delayTime) {
    mouth.write(position);
    delay(delayTime);
  }

  void talk(String sentence = "") {
    String word = "";
    
    for (int i = 0; i < sentence.length(); i++) {
      word += sentence[i];

      if (sentence[i] == ' ') {
        moveMouth(95, 150);  // Move the mouth to emphasize word
        Serial.println(word);
        delay(150);
        moveMouth(50, 100);  // Move the mouth back to the default position
        delay(100);
        word = "";
      }
    }

    // Print the last word (if any)
    if (word.length() > 0) {
      moveMouth(95, 150);
      Serial.println(word);
      delay(150);
      moveMouth(50, 100);
      delay(100);
    }
  }

  void processCommand(String command) {
    if (command.equals("talk")) {
      // Generate a random word for demonstration
      int randomNum = random(0, 4);
      String word = getRandomWord(randomNum);
      talk(word);
    } else if (command.equals("number")) {
      Serial.println("How many words: ");
      while (!Serial.available()) {
        // Wait for user input
      }

      int words = Serial.parseInt();
      for (int i = words; i > 0; i--) {
        String strWords = String(i);
        talk(strWords + " ");
      }

      // Clear the buffer
      while (Serial.available() > 0) {
        Serial.read();
      }
    } else {
      talk(command);
    }
  }

  void serialCommand() {
    if (Serial.available() > 0) {
      String inputString = Serial.readStringUntil('\n'); // Read until newline character
      processCommand(inputString);
    }
  }

private:
  String getRandomWord(int index) {
    switch (index) {
      case 0:
        return "Hello";
      case 1:
        return "Deadpool";
      case 2:
        return "Father";
      case 3:
        return "Hola";
      default:
        return "default";
    }
  }
};



TalkingMouth talkingMouth;  // Create an instance of the TalkingMouth class

void setup() {
  talkingMouth.initialize();
}

void loop() {
  talkingMouth.serialCommand();
}