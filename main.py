import time
import base64
def Hexencode():
  pole = input("What would you like to convert to hex?\n")
  text = bytes(pole, 'utf-8')
  print("--------------------------------")
  print(text.hex())
  print("--------------------------------")
  again = input("Type 1 to convert more text or press 2 to decode!")
  if again == '2':
   time.sleep(1)
   Hexdecode()
  if again == '1':
   time.sleep(1)
   Hexencode()
  else:
    print ("invalid input")
    time.sleep(1)
    menu()

def Hexdecode():
  text = input("Enter String of Hex: ")
  assembly = bytes.fromhex(text)
  print("--------------------------------")
  print(assembly.decode('utf-8'))
  print("--------------------------------")
  again = input("Type 1 to decode more text\n press 2 to convert!\n Press 3 to exit to menu\n")
  if again == '2':
   time.sleep(1)
   Hexdecode()
  if again == '1':
   time.sleep(1)
   Hexencode()
    
  if again == '3':
   time.sleep(1)
  
   menu()
  else:
   print ("invalid input")
   time.sleep(1)
   menu()
    
def Base32encode():
  poles = input("What would you like to convert to Base32?\n")
  encoded = base64.b32encode(bytes(poles, 'utf-8'))
  print("--------------------------------")
  print(encoded.decode('utf-8'))
  print("--------------------------------")
  again = input(" Press 1 to convert more text\n Press 2 to decode\n Press 3 to return to the menu")
  if again == '1':
   time.sleep(1)

   Base32encode()
  if again == '2':
   time.sleep(1)

   Base32decode()

  if again == '3':
   time.sleep(1)

   menu()
  else:
    print ("invalid input")
    time.sleep(1)
    menu()

def Base32decode():
  text = input("Enter String of Base32: ")
  assembly = base64.b32decode(text)
  print("--------------------------------")
  print(assembly.decode('utf-8'))
  print("--------------------------------")
  again = input(" Press 1 to decode more text\n Press 2 to convert\n Press 3 to return to the menu")
  if again == '1':
   time.sleep(1)
   
   Base32decode()
  if again == '2':
   time.sleep(1)
   
   Base32encode()
  if again == '3':
   time.sleep(1)
   
   menu()
  else:
   print ("invalid input")
   time.sleep(1)
   menu()
def Base16encode():
  poles = input("What would you like to convert to Base16?\n")
  encoded = base64.b16encode(bytes(poles, 'utf-8'))
  print("--------------------------------")
  print(encoded.decode('utf-8'))
  print("--------------------------------")
  again = input(" Press 1 to convert more text\n Press 2 to decode\n Press 3 to return to the menu")
  if again == '1':
     time.sleep(1)
     
     Base16encode()
  if again == '2':
   time.sleep(1)
   
   Base16decode()
  if again == '3':
   time.sleep(1)

   menu()
  else:
    print ("invalid input")
    time.sleep(1)

    menu()

def Base16decode():
  text = input("Enter String of Base16: ")
  assembly = base64.b16decode(text)
  print("--------------------------------")
  print(assembly.decode('utf-8'))
  print("--------------------------------")
  again = input(" Press 1 to decode more text\n Press 2 to convert\n Press 3 to return to the menu")
  if again == '2':
   time.sleep(1)
   
   Base16encode()
  if again == '1':
   time.sleep(1)

   Base16decode()
  if again == '3':
   time.sleep(1)

   menu()
  else:
   print ("invalid input")
   time.sleep(1)

   menu()
def Base85encode():
  poles = input("What would you like to convert to Base85?\n")
  encoded = base64.b85encode(bytes(poles, 'utf-8'))
  print("--------------------------------")
  print(encoded.decode('utf-8'))
  print("--------------------------------")
  again = input(" Press 1 to convert more text\n Press 2 to decode\n Press 3 to return to the menu")
  if again == '1':
     time.sleep(1)
     
     print('\033[2J\033[H', end='')
     Base85encode()
  if again == '2':
   time.sleep(1)

   Base85decode()
  if again == '3':
   time.sleep(1)

   menu()
  else:
    print ("invalid input")
    time.sleep(1)

    menu()

def Base85decode():
  text = input("Enter String of Base85: ")
  assembly = base64.b85decode(text)
  print("--------------------------------")
  print(assembly.decode('utf-8'))
  print("--------------------------------")
  again = input(" Press 1 to decode more text\n Press 2 to convert\n Press 3 to return to the menu")
  if again == '2':
   time.sleep(1)
   
   Base85decode()
  if again == '1':
   time.sleep(1)
   
   Base85encode()
  if again == '3':
   time.sleep(1)
   
   menu()
  else:
   print ("invalid input")
   time.sleep(2)
   print('\033[2J\033[H', end='')
   menu()       
def Base64encode():
  poles = input("What would you like to convert to Base64?\n")
  encoded = base64.b64encode(bytes(poles, 'utf-8'))
  print("--------------------------------")
  print(encoded.decode('utf-8'))
  print("--------------------------------")
  again = input(" Press 1 to convert more text\n Press 2 to decode\n Press 3 to return to the menu")
  if again == '1':
   time.sleep(1)
   
   Base64encode()
  if again == '2':
   time.sleep(1)

   Base64decode()
  if again == '3':
   time.sleep(1)

   menu()
  else:
    print ("invalid input")
    time.sleep(1)

    menu()

def Base64decode():
  text = input("Enter String of Base64: ")
  assembly = base64.b64decode(text)
  print("--------------------------------")
  print(assembly.decode('utf-8'))
  print("--------------------------------")
  again = input(" Press 1 to decode more text\n Press 2 to convert\n Press 3 to return to the menu")
  if again == '2':
   time.sleep(1)

   Bae64encode()
  if again == '1':
   time.sleep(1)
 
   Base64decode()
  if again == '1':
   time.sleep(2)

   menu()
  else:
   print ("invalid input")
   time.sleep(1)

   menu()
  
def menu():
  Choice = input(" Press 1 to convert text to hex\n Press 2 to hex to text\n Press 3 to convert text to base85\n Press 4 to decode it\n Press 5 to convert text to base64\n Press 6 to decode it\n Press 7 to convert text to base32\n Press 8 to decode it\n Press 9 to convert text to base16\n Press 10 to decode it:  ")
  if Choice == '1':

    Hexencode()
  if Choice == '2':

    Hexdecode()
  if Choice == '3':

    Base85encode()
  if Choice == '4':

    Base85decode()
  if Choice == '5':

    Base64encode()
  if Choice == '6':

    Base64decode()
  if Choice == '7':

    Base32encode()
  if Choice == '8':

    Base32decode()
  if Choice == '9':

    Base16encode()
  if Choice == '10':

    Base16decode()
  else:
    print("Invalid input")
    time.sleep(1)
    menu()
menu()

