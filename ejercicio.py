import json
datos = json.load(open("datos.json"))


print(f"Como se llama la persona: {datos['nombre']}")

print(f"Que edad tiene: {datos['edad']}")

print(f"Que equipo de futbol le gusta: {datos['equipo_de_futbol']}")

print(f"Cuantos hermanos tiene: {datos['numero_de_hermanos']} ")

print(f"Cuantos coches tiene: {len(datos['coches'])}")

print(f"Es conductor: {'si' if datos['conductor']  else 'no'}")