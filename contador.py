import sys

#vamos a abrir el fichero contador.txt en modo lectura
try:
    with open("contador.txt", "r") as f:
        contador = int(f.read())

except FileNotFoundError:
    with open("contador.txt", "w") as f:
        f.write("0")
        contador = 0

except ValueError:
    print("Error: El valor no es un número")
    sys.exit(1)

if len(sys.argv)>1 and sys.argv[1] == "inc":
    contador += 1

if len(sys.argv)>1 and sys.argv[1] == "dec":
    contador -= 1

print(contador)

with open("contador.txt", "w") as f:
    f.write(str(contador))