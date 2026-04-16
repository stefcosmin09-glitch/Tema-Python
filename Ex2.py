import os

parola_corecta = os.environ.get("PAROLA_SECRETA") 

parola = input("Introdu parola: ")
if parola == parola_corecta:
    print("Parola corecta!")
else:
    print("Parola incorecta!")

if parola_corecta is None:
    print("Nu exista parola setata!")   

 