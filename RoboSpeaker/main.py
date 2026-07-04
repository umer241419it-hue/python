import pyttsx3 as pt

if __name__ == '__main__':
  print("welcome to RoboSpeaker 1.1. created by Mohammad")
  engine = pt.init('sapi5')
  engine.setProperty('rate', 150)
  while True:
    x = input("Enter what you want me to speak: ")
    if x.lower() == "exit":
      break
    if engine._inLoop:
      engine.endLoop()
    engine.say(x)
    engine.runAndWait()
