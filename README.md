# JSON

- Esto serian los datos de json:
    ```json
    {
        "nombre": "Lucas",
        "edad": 45,
        "conductor": false,
        "coches": [
            "Toyota",
            "BMW",
            "Chevrolet"
        ],
        "telefonos": [
            {
                "modelo": "Samsung",
                "orden": 7,
                "sistema": "Android"
            },
            {
                "modelo": "Pixel",
                "orden": 2,
                "sistema": "Android"
            }
        ],
        "equipo_de_futbol": "Real Madrid",
        "numero_de_hermanos": 1,
        "hermanos": [
            "Pepito",
            "Luisito"
        ]
    }
    ''''


- Luego en Python ponemos estos otros datos:
    ```python
        import json
    datos = json.load(open("datos.json"))


    print(f"Como se llama la persona: {datos['nombre']}")

    print(f"Que edad tiene: {datos['edad']}")

    print(f"Que equipo de futbol le gusta: {datos['equipo_de_futbol']}")

    print(f"Cuantos hermanos tiene: {datos['numero_de_hermanos']} ")

    print(f"Cuantos coches tiene: {len(datos['coches'])}")

    print(f"Es conductor: {'si' if datos['conductor']  else 'no'}")
        ''''

- Lo que Python hace es que llame a los datos de json importando el json y asi lo llama para poder hacer preguntas.