from biblio import caesar_logo

print(caesar_logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
char = ["!", "@", "#", "$", "%", "&", "*", "(" , ")", "_", "-", "=", "+", ">", "<", "{", "}", "[", "]", ",", ".", ";", ":", "?", "/", "|"]
number = ["1", "0", "4", "6", "9", "3", "7", "8", "2", "5"]

def caesar(plain_text, shift_amount, choice):
  text = ""
  if choice == "decode":
    shift_amount *= -1
  for letter in plain_text:
    if letter.lower() in alphabet:
      index = alphabet.index(letter.lower())
      index = (index + shift_amount) % 26

      new_letter = alphabet[index]
      if letter.isupper():
          text += new_letter.upper()
      else:
          text += new_letter
    
    elif letter in char:
      index = char.index(letter.lower())
      index = (index + shift_amount) % 26      
      text += char[index]
    
    elif letter in number:
      index = number.index(letter.lower())
      index = (index + shift_amount) % 10
      text += number[index]
    else:
        text += letter

  return text

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
while direction != "encode" and direction != "decode":
    direction = input("Sorry,do you want to 'encode' or to 'decode':\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

print(caesar(text, shift, direction))