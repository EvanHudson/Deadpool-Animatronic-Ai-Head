#include <Servo.h>

Servo mouth;

void setup() {
  Serial.begin(9600);
  mouth.attach(9);
  mouth.write(50);
}

void talk(String sentence ="") {
  //int words=1;
    String word ="";
   for(int i = 0; i<sentence.length(); i++)
   {

    word+=sentence[i];

    if(sentence[i]==' ')
    {

      mouth.write(95);
      delay(150);
      Serial.println(word);
      delay(150);
      mouth.write(50);
      delay(100);
      
      /*****************
      for (int pos = 30; pos < 75; pos += 1) {
        mouth.write(pos);
        delay(5);
      }

      for (int pos = 75; pos > 30; pos += -1) {
        mouth.write(pos);
        delay(10);
    }
    Serial.println(word);
    ***************/
    word="";
      //words++;
    }    

   }
     // Print the last word (if any)
  if (word.length() > 0) {
      mouth.write(95);
      delay(150);
      Serial.println(word);
      delay(150);
      mouth.write(50);
      delay(100);
      }
        /*///////////////////////////
      for (int pos = 75; pos > 30; pos += -1) {
        mouth.write(pos);
        delay(10);
    }

    Serial.println(word);
    */////////////////////
  }

   /************* 
  while(words!=0)
  {

  for (int pos = 30; pos < 80; pos += 1) {
    mouth.write(pos);
    delay(5);
  }

  for (int pos = 80; pos > 30; pos += -1) {
    mouth.write(pos);
    delay(10);
  }
   words+=-1; 
  }
*****************/
//}


void processCommand(String command) {
  // String lowercaseCommand = command.toLowerCase();
  if (command.equals("talk")) {
    int randomNum= random(0, 4);
    String word = "";
    switch (randomNum){
      case 0:
          word="Hello";
          break;
      case 1:
          word="Deadpool";
          break;
      case 2:
          word="Father";
          break;
      case 3:
          word="Hola";
          break;
      default:
          word="default";
    }
    talk(word);
  } 
  
  else if (command.equals("number")) {
    Serial.println("How many words: ");
    while (!Serial.available()) {
      // Wait for user input
    }

    int words = Serial.parseInt();
    //String strWords= String(words);
    for(int i =words; i>0; i--)
    {
      String strWords = String(i);

    talk( strWords +" ");

    }
    //Serial.println("Received integer: " + String(words));

    // Clear the buffer
    while (Serial.available() > 0) {
      Serial.read();
    }
  }
  else
  {

      talk(command);


  }
  // Add more cases for other commands if needed
}

void serialCommand() {
  if (Serial.available() > 0) {
    String inputString = Serial.readStringUntil('\n'); // Read until newline character
    processCommand(inputString);
  }
}

void loop() {
  serialCommand();
}