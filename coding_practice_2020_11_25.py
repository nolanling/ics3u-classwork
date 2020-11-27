#34
number = int(input())
if (number%2 == 0):
  print("even")
else:
  print("odd")
  
#35
age = int(input())
if (age >= 2):
  dog_year = 10.5 + (age-2)*4
  print(dog_year)
elif (0 <= age < 2):
  dog_year = age*5.25
  print(dog_year)
else:
  print("error")

#36
character = input().lower()
if (character == "a"):
  print("vowel")
elif (character == "e"):
  print("vowel")
elif (character == "i"):
  print("vowel")  
elif (character == "o"):
  print("vowel")
elif (character == "u"):
  print("vowel")
elif (character == "y"):
  print("sometimes y is a vowel, and sometimes y is a consonant.")  
else:
  print("constant")
  
#37
side = int(input())
if (side == 3):
  print("triangle")
elif (side == 4):
  print("rectangle")
elif (side == 5):
  print("pentagon")
elif (side == 6):
  print("hexagon")
elif (side == 7):
  print("heptagon")
elif (side == 8):
  print("octagon")
elif (side == 9):
  print("nonagon")
elif (side == 10):
  print("decagon")
else:
  print("error")
  
#38
month = input()
if month == "Janurary" or "March" or "May" or "July" or "August" or "October" or "December":
  print("31 days")
elif month == "Feburary":
  print ("28 or 29 days")
else:
  print("30 days")
  
#39
