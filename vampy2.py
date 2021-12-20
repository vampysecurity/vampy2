#este script es para mis amigos peruanos
""" 
code writting by Vampy Security"""
import  os
import  webbrowser

print("hola usuario")
print("solamente elige la opcion deseada")
print("menu")
print("")
print ("1.- pagina de la NSA")
print("2.- pagina de la CIA")
print("3.- instalar nmap en termux")
print("4.- instalar lenguajes de programacion en termux")
print("5.- complementos de termux")
opcion = int(input("introduce el num deseado:   "))
if opcion == 1:
        webbrowser.open('https://nsa.gov')
elif opcion == 2:
        webbrowser.open('https://cia.gov')
elif opcion == 3:
        os.system('apt install nmap -y')
elif opcion == 4:
        os.system('apt install python python2 perl php ruby -y')
elif opcion == 5:
        os.system('apt install git curl wget vim -y')
else:
        print("esta opcion no es validad judio")
