import sys

def enterInput():
  print("Enter morse code")
  morseCode = input()
  validateInput(morseCode)

def validateInput(morseCode):
  if (morseCode.__contains__(".") or morseCode.__contains__("-")):
    morse_case(morseCode)
  else:
    print("An exception occurred!")
    enterInput()

def moreCode():
  print("Would you like to convert more morse code?")
  answer = input()
  if (answer == "yes"):
    conversionOption()
  elif (answer == "no"):
    print("Thank you and goodbye")
    sys.exit("End")
  else:
    print("Error")
    moreCode()

def morse_case(value):
  try:
    cases = {
        ".-" : lambda: print("A"),
        "-..." : lambda: print("B"),
        "-.-." : lambda: print("C"),
        "-.." : lambda: print("D"),
        "." : lambda: print("E"),
        "..-." : lambda: print("F"),
        "--." : lambda: print("G"),
        "...." : lambda: print("H"),
        ".." : lambda: print("I"),
        ".---" : lambda: print("J"),
        "-.-" : lambda: print("K"),
        ".-.." : lambda: print("L"),
        "--" : lambda: print("M"),
        "-." : lambda: print("N"),
        "---" : lambda: print("O"),
        ".--." : lambda: print("P"),
        "--.-" : lambda: print("Q"),
        ".-." : lambda: print("R"),
        "..." : lambda: print("S"),
        "-" : lambda: print("T"),
        "..-" : lambda: print("U"),
        "...-" : lambda: print("V"),
        ".--" : lambda: print("W"),
        "-..-" : lambda: print("X"),
        "-.--" : lambda: print("Y"),
        "--.." : lambda: print("Z"),
        "-----" : lambda: print("0"),
        ".----" : lambda: print("1"),
        "..---" : lambda: print("2"),
        "...--" : lambda: print("3"),
        "....-" : lambda: print("4"),
        "....." : lambda: print("5"),
        "-...." : lambda: print("6"),
        "--..." : lambda: print("7"),
        "---.." : lambda: print("8"),
        "----." : lambda: print("9"),
    }
    cases[value]()
    moreCode()
  except:
    print("An exception occurred!")
    enterInput()

####################

def enterInput2():
  print("Enter a letter or number")
  English = input()
  validateInput2(English)
  english_case(English)

def validateInput2(English):
  if(English.isalpha):
    english_case(English)
  else:
    print("An exception occurred!")
    enterInput2()

def english_case(value2):
  try:
    cases = {
        "A" : lambda: print(".-"),
        "B" : lambda: print("-..."),
        "C" : lambda: print("-.-."),
        "D" : lambda: print("-.."),
        "E" : lambda: print("."),
        "F" : lambda: print("..-."),
        "G" : lambda: print("--."),
        "H" : lambda: print("...."),
        "I" : lambda: print(".."),
        "J" : lambda: print(".---"),
        "K" : lambda: print("-.-"),
        "L" : lambda: print(".-.."),
        "M" : lambda: print("--"),
        "N" : lambda: print("-."),
        "O" : lambda: print("---"),
        "P" : lambda: print(".--."),
        "Q" : lambda: print("--.-"),
        "R" : lambda: print(".-."),
        "S" : lambda: print("..."),
        "T" : lambda: print("-"),
        "U" : lambda: print("..-"),
        "V" : lambda: print("...-"),
        "W" : lambda: print(".--"),
        "X" : lambda: print("-..-"),
        "Y" : lambda: print("-.--"),
        "Z" : lambda: print("--.."),
        "0" : lambda: print("-----"),
        "1" : lambda: print(".----"),
        "2" : lambda: print("..---"),
        "3" : lambda: print("...--"),
        "4" : lambda: print("....-"),
        "5" : lambda: print("....."),
        "6" : lambda: print("-...."),
        "7" : lambda: print("--..."),
        "8" : lambda: print("---.."),
        "9" : lambda: print("----."),
    }
    cases[value2]()
    moreCode()
  except:
    print("An exception occurred!")
    enterInput2()

def conversionOption():
  print("Would you like to convert Morse to English (MTE) or English to Morse (ETM)?")
  answer = input()
  if(answer == "MTE"):
    enterInput()
  if (answer == "ETM"):
    enterInput2()
  else:
    print("Error")
    conversionOption()

conversionOption()