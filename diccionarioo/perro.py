perro = {}

perro ["nombre"] = "Killer"
perro["color"] = "Blanco"
perro["Raza"] = "Pitbull"
perro["Patas"] = "4"
perro["edad"] = "2"

estudiante = {

"nombre":"Brenda",
"apellido":"Gaviria",
"sexo":"Femenino",
"edad":"18",
"estado civil":"Viuda",
"habilidades":["Empatia, Programacion"],
"pais":"Colombia",
"Ciudad":"Cartegena",
"Direccion":"Las Gaviotas",
}

print(estudiante)
print(len(perro))
print(estudiante["habilidades"])
estudiante["habilidades"].append("Escritora")
print(estudiante["habilidades"])
keys = estudiante.keys()
print(keys)
values = estudiante.values()
print(values)
print(estudiante.items())
estudiante.pop("estado civil")
print(estudiante)
print(estudiante.clear())

