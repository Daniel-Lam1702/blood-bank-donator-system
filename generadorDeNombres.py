import random
def generadorDeNombres():
    """
    Funcionamiento: crear una matriz con los nombres y apellidos
    Entradas: Na
    Salidas: retorna [nombres[random.randint(0,99)],apellidos[random.randint(0,99)],apellidos[random.randint(0,99)]]
    """
    nombres = [["Juan","José Luis","José","Francisco","Antonio","Jesús","Guadalupe","Miguel Ángel","Pedro","Alejandro","Manuel","Juan Carlos","Roberto","Fernando","Daniel",
"Carlos","Jorge","Ricardo","Miguel","Eduardo","Javier","Rafael","Martín","Raúl","David","José Antonio","Arturo","Marco Antonio","José Manuel","Francisco Javier","Enrique","Gerardo",
"Mario","Alfredo","Sergio","Alberto","Luis","Armando","Santiago","Juan Manuel",
"Salvador","Víctor Manuel","Gabriel","Andrés","Óscar","Guillermo","Ramón","Pablo","Ruben",
"Luis Ángel","Felipe","Jorge Jesús","Jaime","José Guadalupe","Julio Cesar","José De Jesús","Diego","Agustín","Gustavo"],
["María Guadalupe","Guadalupe","María","Juana","Margarita","María Del Carmen","Josefina","Verónica","María Elena","Leticia","Rosa","Francisca","Teresa","Alicia","María Fernanda",
"Alejandra","Marta","Yolanda","Patricia","María De Los Ángeles","Rosa María","Elizabeth","Gloria","Ángela","Gabriela","Silvia","María De Guadalupe","María De Jesús",
"Ana María","María Isabel","Antonia","María Luisa","María Del Rosario","Araceli",
"Andrea","Isabel","María Teresa","Irma","Carmen","Lucía","Adriana","María De La Luz",
"María José","Josefina","María","Juanita","Margarina","Carmen","Karen","Lucía","Marípaz","Julieta","Flor","Mónica","Teresita","Alisson","Xinia",
"Alejandrina","Martina"]]   
    apellidos = ["García","González","Rodríguez","Fernández","López","Martínez","Sánchez","Pérez","Gómez","Martin","Jiménez",
"Ruiz","Hernández","Diaz","Moreno","Álvarez","Muñoz","Romero","Alonso","Gutiérrez","Navarro",
"Torres","Domínguez","Vázquez","Ramos","Gil","Ramírez","Serrano","Blanco","Suarez","Molina",
"Morales","Ortega","Delgado","Castro","Ortiz","Rubio","Marín","Sanz","Núñez","Iglesias","Medina",
"Santos","Castillo","Cortes","Lozano","Guerrero","Cano","Prieto","Méndez","Calvo","Cruz","Garrido",
"Gallego","Vidal","León","Herrera","Márquez","Peña","Cabrera","Flores","Campos","Vega","Solís",
"Fuentes","Carrasco","Caballero","Nieto","Reyes","Aguilar","Pascual","Herrero","Santana","Lorenzo","Hidalgo",
"Montero","Ibáñez","Giménez","Ferrer","Duran","Vicente","Benítez","Mora","Ditel","Arias","Vargas",
"Carmona","Crespo","Román","Pastor","Soto","Sáez","Velasco","Soler","Moya","Chavarría","Parra","Bravo","Gallardo","Rojas"]
    sexo=random.randint(0,1)
    if sexo==0:
        sexoBool=True
    else:
        sexoBool=False
    return [nombres[sexo][random.randint(0,58)]+ " "+apellidos[random.randint(0,99)]+" "+apellidos[random.randint(0,99)],sexoBool]