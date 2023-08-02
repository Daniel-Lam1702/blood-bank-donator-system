#Elaborado por Miguel Aguilar y Daniel Lam
#Fecha de creación: 14/05/2021 08:08 pm
#Última fecha de modificación: 14/05/2021 10:25
#Versión 3.9.2
#Importación de librería
import pickle
def graba(nomArchGrabar,estructura):
    """
    Funcionamiento: guarda una lista a la memoria secundaria
    Entradas: 
    -nomArchGrabar: el nombre de archivo en donde se va guardar
    -lista: la lista que se va a guardar
    Salida: NA
    """
    try:
        escritura=open(nomArchGrabar,"wb")
        pickle.dump(estructura,escritura)
        escritura.close()
    except:
        print()
    return
def leeLugar(nomArchLeer):
    """
    Funcionamiento: Graba la informacion en la base de datos
    Entradas:
    -nomArchLeer(nombre del archivo) a leer
    Salida:NA
    """
    lugares ={"San José": ['El banco Nacional de Sangre', 'Hospital México', 'Hospital San Juan de Dios'], "Alajuela": ['Hospital San Rafael de Alajuela','Hospital de San Ramón','Hospital del Cantón Norteño'],'Cartago':['Hospital Max Peralta'],'Heredia':['Hospital San Vicnete de Paúl'],'Guanacaste':['Hospital La Anexión en Nicoya','Hospital Enrique Baltodano de Liberia'],'Puntarenas':['Hospital Monseñor Sanabria'],'Limón':['Hospital Tony Facio','Hospital de Guápiles']}
    try:
        lectura=open(nomArchLeer,"rb")
        lugares = pickle.load(lectura)
        lectura.close()
    except:
        print()
    return lugares
def leeDonante(nomArchLeer):
    """
    Funcionamiento: Graba la informacion en la base de datos
    Entradas:
    -nomArchLeer(nombre del archivo) a leer
    Salida:NA
    """
    donantes = []
    try:
        lectura=open(nomArchLeer,"rb")
        donantes = pickle.load(lectura)
        lectura.close()
    except:
        print()
    return donantes
