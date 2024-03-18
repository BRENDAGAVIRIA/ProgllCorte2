
vuelo = {
    "Aerolinea": "Air France",
    "Vuelo": "AV3085",
    "Origen": "Cartagena",
    "Destino": "Paris",
    "Tipo_Maleta": ['Cabina', 'Mano', 'Bodega']
}


print("Valores del diccionario:")
for key, value in vuelo.items():
    print(f"{key}: {value}")


print("\nValores del tipo de maleta:")
for maleta in vuelo["Tipo_Maleta"]:
    print(maleta)
