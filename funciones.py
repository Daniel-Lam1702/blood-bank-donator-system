#Elaborado por Daniel Eduardo Lam He
#Fecha de creacion: 15/05/2021 10:53 pm
#Última fecha de modificación: 15/05/2021 11:00 pm
#Versión:3.9.2
#Definicion de librerías
from tkinter import messagebox
from memoriaSecundaria import*
import random
from generadorDeNombres import *
import datetime
#Reto 1
def registrarDonador(pDonador):
    """
    funcionamiento: Encargado del funcionamiento de generar donadores
    Entrada: pDonador(matriz)datos del donador
    Salida: NA
    """
    donantes = leeDonante("donantes")
    pDonador[5]=int(pDonador[5])
    pDonador.append(1)
    donantes.append(pDonador)
    graba("donantes",donantes)
    donantes = leeDonante("donantes")
    print(donantes)
    return
#reto 2
def actualizarDonador(pDonador):
    """
    funcionamiento: Encargado del agregar los nuevos datos actualizados 
    Entrada: pDonador(matriz)Informacion del donador
    Salida: NA
    """
    try: 
        donadores = leeDonante("donantes")
        print(pDonador)
        for i in range(len(donadores)):
            print(pDonador)
            if pDonador[1] in donadores[i]:
                donadores[i][0]=pDonador[0]
                donadores[i][2]=pDonador[2]
                donadores[i][3]=pDonador[3]
                donadores[i][4]=pDonador[4]
                donadores[i][5]=int(pDonador[5])
                donadores[i][6]=pDonador[6]
                donadores[i][7]=pDonador[7]
                graba("donantes",donadores)
                return True
    except:
        return False
#Reto 3 
def generarCedula():
    """
    funcionamiento: Encargado de generar los números del cédula
    Entrada: NA
    Salida: NA
    """
    valorDeVerdad=True
    while True:
        num=random.randint(100215412,909990999)
        cedula=str(num)[0]+"-"+str(num)[1:5]+"-"+str(num)[5:]
        for donante in leeDonante("donantes"):
            if cedula in donante:
                valorDeVerdad=False
                break
        if valorDeVerdad:
            return cedula


def generarNombreSexo():
    """
    Funcionamiento: generar nombres ramdom
    Entradas: Na
    Salidas: matriz ramdom
    """
    try:
        return generadorDeNombres()
    except:
        print("Se generó un error")

def fecha():
    """
    funcionamiento: Encargado generar fechas aleatorias
    Entrada: NA
    Salida: NA
    """
    start_date = datetime.date(datetime.date.today().year-64, 1, 1)
    end_date = datetime.date(datetime.date.today().year-18, datetime.date.today().month, datetime.date.today().day-1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return str(random_date)[8:]+"/"+str(random_date)[5:7]+"/"+str(random_date)[0:4]
def tipoSangre():
    """
    funcionamiento: Encargado de generar diferentes tipos de sangre
    Entrada: NA
    Salida: NA
    """
    numero = random.randint(0,7)
    if numero == 0:
        return "O+"
    elif numero == 1:
        return "O-"
    elif numero == 2:
        return "A+"
    elif numero == 3:
        return "A-"
    elif numero == 4:
        return "B+"
    elif numero == 5:
        return "B-"
    elif numero == 6:
        return "AB+"
    else:
        return "AB-"
def peso():
    """
    funcionamiento: Encargado del un peso aletoria
    Entrada: NA
    Salida: NA
    """
    return random.randint(51,119)
def correo(pNombre):
    """
    funcionamiento: Encargado de generar correos aleatorios
    Entrada: pNombre(str) Nombre del correo
    Salida: NA
    """
    nombre=""
    correo=["costarricense.cr","racsa.go.cr","ccss.sa.cr","gmail.com","hotmail.com","estudiantec.cr","outlook.com","icloud.com"]
    listaNombre=pNombre.split(" ")
    for i in listaNombre:
        nombre+=i
    return (nombre)+str(random.randint(10,999))+"@"+correo[random.randint(0,7)]
def telefono():
    """
    funcionamiento: Encargado de generar telefonos aleatorios
    Entrada: NA
    Salida: NA
    """
    num=random.randint(254000000,899999999)
    return str(num)[0:4]+"-"+str(num)[5:]
    
def crearDonar(pCant):
    """
    funcionamiento: Encargado de generar la lista con la informacion de los donadores
    Entrada: pCant(int)cantidad de donadores
    Salida: NA
    """
    try:
        donar=leeDonante("donantes")
        for i in range(pCant):
            nombreSexo=generarNombreSexo()
            donar.append([nombreSexo[0]]+[generarCedula()]+[tipoSangre()]+[nombreSexo[1]]+[fecha()]+[peso()]+[correo(nombreSexo[0].lower())]+[telefono()]+[1])
        graba("donantes",donar)
        return True 
    except:
        return False
#Reto 4
def eliminarDonador(pDonador,pJustificacion):
    """
    funcionamiento: Encargada del funcionamiento de eliminar donador
    Entrada: pDonador(matriz) informacion del donador
    pJustificación(int) 
    Salida: NA
    """
    donantes = leeDonante("donantes")
    for donante in donantes:
        if pDonador in donante:
            donante[8]=0
            if len(donante)<10:
                donante.append(pJustificacion)
            else:
                donante[-1]=pJustificacion                
            break
    graba("donantes",donantes)
    donantes = leeDonante("donantes")
    return    
#Reto 5
def  insertarLugar(pProvincia,pLugar):
    """
    funcionamiento: Encargado de el funcionamiento de generar lugares
    Entrada: pProvincia(Str)Provincia
    pLugar(str) Lugar nuevo
    Salida: NA
    """
    try: 
        lugares= leeLugar("lugares")
        lugares[pProvincia].append(pLugar)
        graba("lugares",lugares)
        return True
    except:
        return False
        
