import random
import string

def generate_password(min_length,numbers=True,special_characters=True):
   letters = string.ascii_letters
   digits =  string.digits
   special =string.punctuation
   characters = letters
   if numbers :
      characters += digits
   if special_characters:
      characters+= special

   pwd = ""
   meets_criteria =False
   has_number = False
   has_Special =False

   while not meets_criteria or len(pwd) < min_length:      



generate_password(10)