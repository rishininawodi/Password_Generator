#import two modules

import random
import string  #grab all the lowecase and upper case letters that exists and all special characters and also numbers and digits

 #first need to ask the user what is the minimum length is,if they want numbers,if the wants special characters........

 #Second thing need to write a function which is actually going to generate the password

#password generate function
def generate_password(min_length,numbers=True,special_characters=True):
   
   #grab all the potential characters...
   letters = string.ascii_letters
   digits =  string.digits
   special =string.punctuation

  # print(letters,digits,special)# by using this we can see all characters and letters...

  #geting the enters leters or characters in to pne string or array
   characters = letters #because allways have letters.
   if numbers :
      characters += digits  #if numbrs true then add it for leeters
   if special_characters:
      characters+= special

#generate loop...
   pwd = ""
   meets_criteria =False
   has_number = False
   has_Special =False

   while not meets_criteria or len(pwd) < min_length:  #while we are nott meeting criteria,so while we dont have  special characters or dont have a number or whatever that criteria is,or the length of our password is not yet equal or grater than the minimum length,we continue doing thisaddin characters to our password   
      new_char = random.choice(characters)
      pwd += new_char

      if new_char in digits:
         has_number= True
      elif new_char in special:
         has_Special = True 


      meets_criteria = True
      if numbers:
         meets_criteria = has_number
      if special_characters:
         meets_criteria = meets_criteria and has_Special  # return treu if only both true      


#return generated password...
   return pwd

min_length = int(input("Enter the minimum length you want: "))
has_number = input("Dou want to add numbers (y/n)? ")  .lower() =="y"
has_special = input("Dou want to add Special characters (y/n)? ")  .lower() =="y"

pwd = generate_password(min_length,has_number,has_special)
print(pwd)


