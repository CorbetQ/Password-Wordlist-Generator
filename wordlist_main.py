from os import system
import wordlist_processor

output = input("Add your output folder : ")

def wordlist():
    print(" _____________________________ ")
    print("| Password Wordlist Generator |")
    print("| * If no answer press ENTER  |")
    print("| * Date Format : DD-MM-YYYY  |")
    print("|_____________________________|")
    firstname    = input("Your first name         : ")
    secondname   = input("Your second name        : ")
    thirdname    = input("Your third name         : ")
    familyname   = input("Your family name        : ")
    surname      = input("Your surname            : ")
    birthdaydate = input("Your birthday date      : ")
    age          = input("Your age                : ")
    department   = input("Your department (nb)    : ")
    country      = input("Your country            : ")
    partner_name = input("Your partner's name     : ")
    partner_sname= input("Your partner's s. name  : ")
    partner_tname= input("Your partner's t. name  : ")
    partner_fname= input("Your partner's f. name  : ")
    partner_srnm = input("Your partner's surname  : ")
    partner_birth= input("Your partner's birthday : ")
    kid_name     = input("Your kid's name         : ")
    kid_surname  = input("Your kid's surname      : ")
    kid_birthday = input("Your kid's birthday     : ")
    gender       = input("Your gender             : ")
    company      = input("Your company's name     : ")
wordlist()