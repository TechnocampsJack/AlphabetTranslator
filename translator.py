dictionary1 = {
  "a": "Fish",
  "b": "Donkey",
  "c": "Duck",
  "d": "Cat",
  "e": "Dog",
  "f": "Horse",
  "g": "Rabbit",
  "h": "Emu",
  "i": "Cow",
  "j": "Sparrow",
  "k": "Pigeon",
  "l": "Hamster",
  "m": "Penguin",
  "n": "Sheep",
  "o": "Goat",
  "p": "Pig",
  "q": "Parrot",
  "r": "Oyster",
  "s": "Crab",
  "t": "Octopus",
  "u": "Dolphin",
  "v": "Whale",
  "w": "Eagle",
  "x": "Owl",
  "y": "Blackbird",
  "z": "Zebra",
  " ": "Snake",
  ".": "Rat"
}




def encode():
  answer = input("What would you like to encode?")
  output=""
  for i in range(0,len(answer)):
    singleLetter = answer[i].lower()
    output += dictionary1[singleLetter] + "/"
  print(output)
  
  
def decode():
  answer = input("What would you like to decode?")
  output=""
  codeWords = str.split(answer, "/")
  print(codeWords)
  for word in codeWords:
    for key,value in dicttionary1.items():
      if value == word:
        output += key
  print(output)

begin = input("Do you want to encode or decode? Press 'e' or 'd' now.")
if begin == "e":
  encode()
elif begin == "d":
  decode()
