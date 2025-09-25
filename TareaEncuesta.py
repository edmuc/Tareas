lista = []

for i in range(10):
    nombre = input("Ingrese su nombre: ")
    idea = input("Ingrese su idea de proyecto: ")
    lista.append((nombre, idea))

print("\n--- Lista de ideas de proyecto ---")
for i in range(10):
    print(f"{i+1}. {lista[i][0]} - {lista[i][1]}")