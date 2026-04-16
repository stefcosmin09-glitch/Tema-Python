#----
#1. Defi neste cate o variabila din fi ecare tip invatat:
#2. Pentru fi ecare variabila afi șați valoarea și tipul ei folosind metoda print
#3. Creați o alta variabila cu numele documentație de tip string pe mai multe linii in care sa puneti pentru fi ecare variabila ceva de genul:
#Variabila X1 este de tipul Y1 si are valoare Z1
#Variabila X2 este de tipul Y2 si are valoare Z2
#4. Afisati si acest string documentatie in consola.
#----





#string
nume = "Stef"
print("nume =", nume)
print(type(nume))

#integer
age = 28
print("age =", age)
print(type(age))

#boolean
a = 3 
b = 4
este_mai_mic = a < b
este_mai_mare = a > b
print("este_mai_mic =", este_mai_mic)
print("este_mai_mare =", este_mai_mare)
print("type(este_mai_mare)", type(este_mai_mare))
print("type(este_mai_mic)", type(este_mai_mic))

#none
valoare = None
print("valoare =", valoare)
print("type(valoare)", type(valoare))

#list
fructe = ["mar", "banana", "portocala"]
print("fructe =", fructe)
print("type(fructe)", type(fructe))

#set
numere = {1, 2, 3, 4, 5}
print("numere =", numere)
print("type(numere)", type(numere))

#Dictionary
persoana = {"nume": "John", "varsta": 30, "oras": "New York"}
print("persoana =", persoana)
print("type(persoana)", type(persoana))

#tuple
coordonate = (10, 20)
print("coordonate =", coordonate)
print("type(coordonate)", type(coordonate))

documentatie = f"""Variabila nume este de tipul {type(nume)} si are valoare {nume}
Variabila age este de tipul {type(age)} si are valoare {age}"""
print("documentatie =", documentatie) 