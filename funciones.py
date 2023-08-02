#Elaborado por Daniel Eduardo Lam He
#Fecha de creacion: 15/05/2021 10:53 pm
#Última fecha de modificación: 15/05/2021 11:00 pm
#Versión:3.9.2
#Definicion de librerías
from memoriaSecundaria import*
#Reto 1
def registrarDonador(pDonador):
    donantes = leeDonante("donantes")
    pDonador[5]=int(pDonador[5])
    pDonador.append(1)
    donantes.append(pDonador)
    graba("donantes",donantes)
    donantes = leeDonante("donantes")
    return
#Reto 4
def eliminarDonador(pDonador,pJustificacion):
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
    print(donantes)
    return    
            