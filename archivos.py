#Elaborado por Miguel Aguilar y Daniel Lam
#Fecha de creación: 16/05/2021 10:24 pm
#Última fecha de modificación: 17/05/2021 4:25 pm
#Versión 3.9.2
#Importación de librería
import pickle
from memoriaSecundaria import*
import datetime
import re
def codificador(palabra):
    diccVocalesTildes={"á":"a","é":"e","í":"i","ó":"o","ú":"u","Á":"a","É":"e","Í":"i","Ó":"o","Ú":"u"}
    diccVocalesDieresis={"ä":"a","ë":"e","ï":"i","ö":"o","ü":"u","Ä":"a","Ë":"e","Ï":"i","Ö":"o","Ü":"u"}
    palabraCodificada=""
    for letra in palabra:
        if letra in diccVocalesTildes:
            palabraCodificada+="&"+diccVocalesTildes[letra]+"acute;"
        elif letra in diccVocalesDieresis:
            palabraCodificada+="&"+diccVocalesDieresis[letra]+"uml;"
        elif letra=="ñ":
            palabraCodificada+="&ntilde;"            
        else:
            palabraCodificada+=letra
    return palabraCodificada
#Reporte 1
def generarListaDonantesProvincia(pProvinciaNum,pProvincia):
    try:
        donantes = leeDonante("donantes")
        listaDonantes=[]
        provinciaCodificada=""
        for donante in donantes:
            if donante[8]!=0:
                if pProvinciaNum==donante[1][0]:
                    listaDonantes.append(donante)
        for donanteprovincia in range(len(listaDonantes)):
            if re.search("[áéíóúÁÉÍÓÚäëïöüÄËÏÖÜñ]",listaDonantes[donanteprovincia][0])!=None:
                listaDonantes[donanteprovincia][0]=codificador(listaDonantes[donanteprovincia][0])
            if re.search("[áéíóúÁÉÍÓÚäëïöüÄËÏÖÜñ]",listaDonantes[donanteprovincia][6])!=None:
                listaDonantes[donanteprovincia][6]=codificador(listaDonantes[donanteprovincia][6])
        if pProvincia=="San José":
            provinciaCodificada = pProvincia[:-1]+"&eacute;"
        elif pProvincia=="Limón":
            provinciaCodificada = "Lim&oacute;n"
        else:
            provinciaCodificada = pProvincia
        return generarReporteProvincia(listaDonantes,pProvincia,provinciaCodificada)
    except:
        return False
def generarReporteProvincia(pLista,pProvincia,pProvinciaCod):
    """
    Funcionamiento: guarda una lista a la memoria secundaria
    Entradas: 
    -nomArchGrabar: el nombre de archivo en donde se va guardar
    -lista: la lista que se va a guardar
    Salida: NA
    """
    try:
        escritura=open("DonantesPorProvincia"+pProvincia+".html","w")
        escritura.write("<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>Donadores por provincia</title>\n\t\t<meta charset=\"UTF-8\">\n\t</head>\n<style type=\"text/css\">\n\ttable, th, td{\n\t\tborder: 1px solid black;\n\t\tborder-collapse: collapse;\n\t}\n</style>")
        escritura.write("\n\t<body>\n\t\t<center>\n\t\t\t<h1>Donantes activos de "+pProvinciaCod+"</h1>\n\t\t\t<h2>Fecha y hora: "+str(datetime.datetime.now())[:-7]+"</h2>\n\t\t\t<table style=\"width: 100%\">")
        escritura.write("\n\t\t\t\t<tr>\n\t\t\t\t\t<th>C&eacute;dula</th>\n\t\t\t\t\t<th>Nombre completo</th>\n\t\t\t\t\t<th>Fecha de nacimiento</th>\n\t\t\t\t\t<th>Tel&eacute;fono</th>\n\t\t\t\t\t<th>Correo</th>\n\t\t\t\t</tr>")
        for donante in pLista:
            escritura.write("\n\t\t\t\t<tr>\n\t\t\t\t\t<td>"+donante[1]+"</td>\n\t\t\t\t\t<td>"+donante[0]+"</td>\n\t\t\t\t\t<td>"+donante[4]+"</td>\n\t\t\t\t\t<td>"+donante[7]+"</td>\n\t\t\t\t\t<td>"+donante[6]+"</td>\n\t\t\t\t</tr>")
        escritura.write("\n\t\t\t</table>\n\t\t</center>\n\t</body>\n</html>")
        escritura.close()
        return True
    except:
        return False
#Reporte 2
def calcularEdad(fechaNac):
    fechaActual=datetime.datetime.now()
    if fechaActual.month >= int(fechaNac[3:5]):
        return fechaActual.year-int(fechaNac[6:])
    return fechaActual.year-int(fechaNac[6:])-1
def generarListaDonantesEdad(pEdadInicial,pEdadFinal):
    try:
        donantes = leeDonante("donantes")
        listaDonantes=[]
        for donante in donantes:
            if donante[8]!=0:
                if calcularEdad(donante[4])>=pEdadInicial and calcularEdad(donante[4])<=pEdadFinal:
                    listaDonantes.append(donante)
        for donanteEdad in range(len(listaDonantes)):
            if re.search("[áéíóúÁÉÍÓÚäëïöüÄËÏÖÜñ]",listaDonantes[donanteEdad][0])!=None:
                listaDonantes[donanteEdad][0]=codificador(listaDonantes[donanteEdad][0])
            if re.search("[áéíóúÁÉÍÓÚäëïöüÄËÏÖÜñ]",listaDonantes[donanteEdad][6])!=None:
                listaDonantes[donanteEdad][6]=codificador(listaDonantes[donanteEdad][6])
        return generarReporteEdad(listaDonantes,pEdadInicial,pEdadFinal)
    except:
        return False
def generarReporteEdad(pLista,pEdadInicial,pEdadFinal):
    """
    Funcionamiento: guarda una lista a la memoria secundaria
    Entradas: 
    -nomArchGrabar: el nombre de archivo en donde se va guardar
    -lista: la lista que se va a guardar
    Salida: NA
    """
    try:
        escritura=open("DonantesPorEdad"+str(pEdadInicial)+"_"+str(pEdadFinal)+".html","w")
        escritura.write("<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>Donadores por Edad</title>\n\t\t<meta charset=\"UTF-8\">\n\t</head>\n<style type=\"text/css\">\n\ttable, th, td{\n\t\tborder: 1px solid black;\n\t\tborder-collapse: collapse;\n\t}\n</style>")
        if pEdadFinal==pEdadInicial:
            escritura.write("\n\t<body>\n\t\t<center>\n\t\t\t<h1>Donantes activos de "+str(pEdadInicial)+" a&ntilde;os"+"</h1>\n\t\t\t<h2>Fecha y hora: "+str(datetime.datetime.now())[:-7]+"</h2>\n\t\t\t<table style=\"width: 100%\">")
        else:
            escritura.write("\n\t<body>\n\t\t<center>\n\t\t\t<h1>Donantes activos de "+str(pEdadInicial)+" a "+str(pEdadFinal)+" a&ntilde;os"+"</h1>\n\t\t\t<h2>Fecha y hora: "+str(datetime.datetime.now())[:-7]+"</h2>\n\t\t\t<table style=\"width: 100%\">")
        escritura.write("\n\t\t\t\t<tr>\n\t\t\t\t\t<th>C&eacute;dula</th>\n\t\t\t\t\t<th>Nombre completo</th>\n\t\t\t\t\t<th>Fecha de nacimiento</th>\n\t\t\t\t\t<th>Tel&eacute;fono</th>\n\t\t\t\t\t<th>Correo</th>\n\t\t\t\t</tr>")
        for donante in pLista:
            escritura.write("\n\t\t\t\t<tr>\n\t\t\t\t\t<td>"+donante[1]+"</td>\n\t\t\t\t\t<td>"+donante[0]+"</td>\n\t\t\t\t\t<td>"+donante[4]+"</td>\n\t\t\t\t\t<td>"+donante[7]+"</td>\n\t\t\t\t\t<td>"+donante[6]+"</td>\n\t\t\t\t</tr>")
        escritura.write("\n\t\t\t</table>\n\t\t</center>\n\t</body>\n</html>")
        escritura.close()
        return True
    except:
        return False
#Reporte 3
def generarListaDonantesSangre(pSangre):
    try:
        donantes = leeDonante("donantes")
        listaDonantes=[]
        for donante in donantes:
            if donante[8]!=0:
                if pSangre==donante[2]:
                    listaDonantes.append(donante)
        for donanteSangre in range(len(listaDonantes)):
            if re.search("[áéíóúÁÉÍÓÚäëïöüÄËÏÖÜñ]",listaDonantes[donanteSangre][0])!=None:
                listaDonantes[donanteSangre][0]=codificador(listaDonantes[donanteSangre][0])
            if re.search("[áéíóúÁÉÍÓÚäëïöüÄËÏÖÜñ]",listaDonantes[donanteSangre][6])!=None:
                listaDonantes[donanteSangre][6]=codificador(listaDonantes[donanteSangre][6])
        return generarReporteProvincia(listaDonantes,pSangre)
    except:
        return False
def generarReporteProvincia(pLista,pSangre):
    """
    Funcionamiento: guarda una lista a la memoria secundaria
    Entradas: 
    -nomArchGrabar: el nombre de archivo en donde se va guardar
    -lista: la lista que se va a guardar
    Salida: NA
    """
    try:
        escritura=open("DonantesPorSangre"+pSangre+".html","w")
        escritura.write("<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>Donadores por provincia</title>\n\t\t<meta charset=\"UTF-8\">\n\t</head>\n<style type=\"text/css\">\n\ttable, th, td{\n\t\tborder: 1px solid black;\n\t\tborder-collapse: collapse;\n\t}\n</style>")
        escritura.write("\n\t<body>\n\t\t<center>\n\t\t\t<h1>Donantes activos de la sangre tipo: "+pSangre+"</h1>\n\t\t\t<h2>Fecha y hora: "+str(datetime.datetime.now())[:-7]+"</h2>\n\t\t\t<table style=\"width: 100%\">")
        escritura.write("\n\t\t\t\t<tr>\n\t\t\t\t\t<th>C&eacute;dula</th>\n\t\t\t\t\t<th>Nombre completo</th>\n\t\t\t\t\t<th>Fecha de nacimiento</th>\n\t\t\t\t\t<th>Tel&eacute;fono</th>\n\t\t\t\t\t<th>Correo</th>\n\t\t\t\t</tr>")
        for donante in pLista:
            escritura.write("\n\t\t\t\t<tr>\n\t\t\t\t\t<td>"+donante[1]+"</td>\n\t\t\t\t\t<td>"+donante[0]+"</td>\n\t\t\t\t\t<td>"+donante[4]+"</td>\n\t\t\t\t\t<td>"+donante[7]+"</td>\n\t\t\t\t\t<td>"+donante[6]+"</td>\n\t\t\t\t</tr>")
        escritura.write("\n\t\t\t</table>\n\t\t</center>\n\t</body>\n</html>")
        escritura.close()
        return True
    except:
        return False
#Reporte 4
def generarListaCompleta():
    try:
        donantes = leeDonante("donantes")
        listaDonantes=[]
        for donante in donantes:
            if donante[8]!=0:
                listaDonantes.append(donante)
        for donante in range(len(listaDonantes)):
            if re.search("[áéíóúÁÉÍÓÚäëïöüÄËÏÖÜñ]",listaDonantes[donante][0])!=None:
                listaDonantes[donante][0]=codificador(listaDonantes[donante][0])
            if re.search("[áéíóúÁÉÍÓÚäëïöüÄËÏÖÜñ]",listaDonantes[donante][6])!=None:
                listaDonantes[donante][6]=codificador(listaDonantes[donante][6])
        return generarReporteProvincia(listaDonantes)
    except:
        return False
def definirSexo(pSexo):
    if pSexo:
        return "Masculino"
    return "Femenino"
def generarReporteProvincia(pLista):
    """
    Funcionamiento: guarda una lista a la memoria secundaria
    Entradas: 
    -nomArchGrabar: el nombre de archivo en donde se va guardar
    -lista: la lista que se va a guardar
    Salida: NA
    """
    try:
        escritura=open("DonantesActivos.html","w")
        escritura.write("<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>Lista de donantes activos</title>\n\t\t<meta charset=\"UTF-8\">\n\t</head>\n<style type=\"text/css\">\n\ttable, th, td{\n\t\tborder: 1px solid black;\n\t\tborder-collapse: collapse;\n\t}\n</style>")
        escritura.write("\n\t<body>\n\t\t<center>\n\t\t\t<h1>Lista de donantes activos</h1>\n\t\t\t<h2>Fecha y hora: "+str(datetime.datetime.now())[:-7]+"</h2>\n\t\t\t<table style=\"width: 100%\">")
        escritura.write("\n\t\t\t\t<tr>\n\t\t\t\t\t<th>C&eacute;dula</th>\n\t\t\t\t\t<th>Nombre completo</th>\n\t\t\t\t\t<th>Tipo de sangre</th>\n\t\t\t\t\t<th>Fecha de nacimiento</th>\n\t\t\t\t\t<th>Peso</th>\n\t\t\t\t\t<th>Sexo</th>\n\t\t\t\t\t<th>Tel&eacute;fono</th>\n\t\t\t\t\t<th>Correo</th>\n\t\t\t\t</tr>")
        for donante in pLista:
            escritura.write("\n\t\t\t\t<tr>\n\t\t\t\t\t<td>"+donante[1]+"</td>\n\t\t\t\t\t<td>"+donante[0]+"</td>\n\t\t\t\t\t<td>"+donante[2]+"</td>\n\t\t\t\t\t<td>"+donante[4]+"</td>\n\t\t\t\t\t<td>"+str(donante[5])+" kg</td>\n\t\t\t\t\t<td>"+definirSexo(donante[3])+"</td>\n\t\t\t\t\t<td>"+donante[7]+"</td>\n\t\t\t\t\t<td>"+donante[6]+"</td>\n\t\t\t\t</tr>")
        escritura.write("\n\t\t\t</table>\n\t\t</center>\n\t</body>\n</html>")
        escritura.close()
        return True
    except:
        return False