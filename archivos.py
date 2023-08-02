#Elaborado por Miguel Aguilar y Daniel Lam
#Fecha de creación: 16/05/2021 10:24 pm
#Última fecha de modificación: 17/05/2021 4:25 pm
#Versión 3.9.2
#Importación de librería
from memoriaSecundaria import*
import datetime
import re
def codificador(palabra):
    """
    Funcionamiento: codificar las letras con caracteres especiales
    Entradas: 
    -palabra(str) letra a codificar
    Salida: NA
    """
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
    """
    Funcionamiento: Generar el reporte 1
    Entradas: 
    -pProvinciaNum El numero de la provincia 
    -pProvinica la provincia
    Salida: NA
    """
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
    Funcionamiento: Creacion del HTML
    Entradas: 
    -pListas(lista) lista de los donantes por provincia
    -pProvincia (str) la provincia
    pProvinciaCod (codigo de la provincia)
    Salida: Valor booleano
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
    """
    Funcionamiento: calcular la edad
    Entradas: 
    -fechaNac(int) fecga de nacimiento
    Salida: NA
    """
    fechaActual=datetime.datetime.now()
    if fechaActual.month >= int(fechaNac[3:5]):
        return fechaActual.year-int(fechaNac[6:])
    return fechaActual.year-int(fechaNac[6:])-1
def generarListaDonantesEdad(pEdadInicial,pEdadFinal):
    """
    Funcionamiento: Encargado de generar el reporte 2
    Entradas: 
    -pEdadInicial(int) la edad inicial
    -pEdadFinal(int)la edad final
    Salida: NA
    """
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
    Funcionamiento: Creacion del HTML
    Entradas: 
    -pListas(lista) lista de los donantes por provincia
    -pEdadInicial (int) la edad inicail
    pEdadFinal (int) edad final
    Salida: Valor booleano
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
    """
    Funcionamiento: Encargado de generar el reporte 3
    Entradas: 
    -pSangre(str) el tipo de sangre
    Salida: NA
    """
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
        return generarReporteSangre(listaDonantes,pSangre)
    except:
        return False
def generarReporteSangre(pLista,pSangre):
    """
    Funcionamiento: Creacion del HTML
    Entradas: 
    -pListas(lista) lista de los donantes de sangre
    -pSangre(str) El tipo de sangre
    Salida: Valor booleano
    """
    try:
        escritura=open("DonantesPorSangre"+pSangre+".html","w")
        escritura.write("<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>Donadores por sangre</title>\n\t\t<meta charset=\"UTF-8\">\n\t</head>\n<style type=\"text/css\">\n\ttable, th, td{\n\t\tborder: 1px solid black;\n\t\tborder-collapse: collapse;\n\t}\n</style>")
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
    """
    Funcionamiento: Encargado de generar el reporte 4
    Entradas:NA
    Salida: NA
    """
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
        return generarReporteCompleto(listaDonantes)
    except:
        return False
def definirSexo(pSexo):
    """
    Funcionamiento: Codificar el seco
    Entradas: 
    -pSexo(str)tipo de sexo
    Salida:NA
    """
    if pSexo:
        return "Masculino"
    return "Femenino"
def generarReporteCompleto(pLista):
    """
    Funcionamiento: Creacion del HTML
    Entradas: 
    -pListas(lista) lista de los donantes activos
    Salida: Valor booleano
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
#Reporte5
"""
def generarListaDonantesSangreO(pSangre):
    
    Funcionamiento: Encargado de generar el reporte 5
    Entradas:pSangre(str) el tipo de sangre
    Salida: NA
    
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
        return generarReporteSangreO(listaDonantes,pSangre)
    except:
        return False
"""
def generarReporteSangreO(pLista):
    """
    Funcionamiento: Creacion del HTML
    Entradas: 
    -pListas(lista) lista de los donantes mujeres O
    Salida: Valor booleano
    """
    try:
        escritura=open("DonantesMujeresPorSangreO-.html","w")
        escritura.write("<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>Donantes mujeres de sangre tipo O-</title>\n\t\t<meta charset=\"UTF-8\">\n\t</head>\n<style type=\"text/css\">\n\ttable, th, td{\n\t\tborder: 1px solid black;\n\t\tborder-collapse: collapse;\n\t}\n</style>")
        escritura.write("\n\t<body>\n\t\t<center>\n\t\t\t<h1>Donantes mujeres de sangre tipo O-</h1>\n\t\t\t<h2>Fecha y hora: "+str(datetime.datetime.now())[:-7]+"</h2>\n\t\t\t<table style=\"width: 100%\">")
        escritura.write("\n\t\t\t\t<tr>\n\t\t\t\t\t<th>C&eacute;dula</th>\n\t\t\t\t\t<th>Nombre completo</th>\n\t\t\t\t\t<th>Fecha de nacimiento</th>\n\t\t\t\t\t<th>Tel&eacute;fono</th>\n\t\t\t\t\t<th>Correo</th>\n\t\t\t\t</tr>")
        for donante in pLista:
            escritura.write("\n\t\t\t\t<tr>\n\t\t\t\t\t<td>"+donante[1]+"</td>\n\t\t\t\t\t<td>"+donante[0]+"</td>\n\t\t\t\t\t<td>"+donante[4]+"</td>\n\t\t\t\t\t<td>"+donante[7]+"</td>\n\t\t\t\t\t<td>"+donante[6]+"</td>\n\t\t\t\t</tr>")
        escritura.write("\n\t\t\t</table>\n\t\t</center>\n\t</body>\n</html>")
        escritura.close()
        return True
    except:
        return False   
def donantesMujereO():
    """
    Funcionamiento: Encargado de generar el reporte 5
    Entradas:NA
    Salida: NA
    """
    try:
        donantes = leeDonante("donantes")
        listaDonantes=[]
        for donante in donantes:
            if donante[8]!=0:
                if "O-"==donante[2]:
                    if donante[3]==False:
                        listaDonantes.append(donante)
        for donanteSangre in range(len(listaDonantes)):
            if re.search("[áéíóúÁÉÍÓÚäëïöüÄËÏÖÜñ]",listaDonantes[donanteSangre][0])!=None:
                listaDonantes[donanteSangre][0]=codificador(listaDonantes[donanteSangre][0])
            if re.search("[áéíóúÁÉÍÓÚäëïöüÄËÏÖÜñ]",listaDonantes[donanteSangre][6])!=None:
                listaDonantes[donanteSangre][6]=codificador(listaDonantes[donanteSangre][6])
        return generarReporteSangreO(listaDonantes)
    except:
        return False 
#Donantes no activos
def generarDonantesNoActivos():
    """
    Funcionamiento: Encargado de generar el reporte 8
    Entradas:NA
    Salida: NA
    """
    try:
        donantes = leeDonante("donantes")
        listaDonantes=[]
        for donante in donantes:
            if donante[8]==0:
                listaDonantes.append(donante)
        for donante in range(len(listaDonantes)):
            if re.search("[áéíóúÁÉÍÓÚäëïöüÄËÏÖÜñ]",listaDonantes[donante][0])!=None:
                listaDonantes[donante][0]=codificador(listaDonantes[donante][0])
            if re.search("[áéíóúÁÉÍÓÚäëïöüÄËÏÖÜñ]",listaDonantes[donante][6])!=None:
                listaDonantes[donante][6]=codificador(listaDonantes[donante][6])
        return generarReporteNoActivos(listaDonantes)
    except:
        return False


def generarReporteNoActivos(pLista):
    """
    Funcionamiento: guarda una lista a la memoria secundaria y crear HTML
    Entradas: 
    -pLista(lista) lista que se va a guardar
    Salida: NA
    """
    try:
        escritura=open("DonantesNoActivos.html","w")
        escritura.write("<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>Lista de donantes no activos</title>\n\t\t<meta charset=\"UTF-8\">\n\t</head>\n<style type=\"text/css\">\n\ttable, th, td{\n\t\tborder: 1px solid black;\n\t\tborder-collapse: collapse;\n\t}\n</style>")
        escritura.write("\n\t<body>\n\t\t<center>\n\t\t\t<h1>Lista de donantes no activos</h1>\n\t\t\t<h2>Fecha y hora: "+str(datetime.datetime.now())[:-7]+"</h2>\n\t\t\t<table style=\"width: 100%\">")
        escritura.write("\n\t\t\t\t<th>justificaci&oacute;n</th>\n\t\t\t\t\t<th>C&eacute;dula</th>\n\t\t\t\t\t<th>Nombre completo</th>\n\t\t\t\t\t<th>Tipo de sangre</th>\n\t\t\t\t\t<th>Fecha de nacimiento</th>\n\t\t\t\t\t<th>Peso</th>\n\t\t\t\t\t<th>Sexo</th>\n\t\t\t\t\t<th>Tel&eacute;fono</th>\n\t\t\t\t\t<th>Correo</th>\n\t\t\t\t</tr>")
        for donante in pLista:
            escritura.write("\n\t\t\t\t<td>"+codificarJustificacion(donante[-1])+"<td>\n\t\t\t\t\t<td>"+donante[1]+"</td>\n\t\t\t\t\t<td>"+donante[0]+"</td>\n\t\t\t\t\t<td>"+donante[2]+"</td>\n\t\t\t\t\t<td>"+donante[4]+"</td>\n\t\t\t\t\t<td>"+str(donante[5])+" kg</td>\n\t\t\t\t\t<td>"+definirSexo(donante[3])+"</td>\n\t\t\t\t\t<td>"+donante[7]+"</td>\n\t\t\t\t\t<td>"+donante[6]+"</td>\n\t\t\t\t</tr>")
        escritura.write("\n\t\t\t</table>\n\t\t</center>\n\t</body>\n</html>")
        escritura.close()
        return True
    except:
        return False
def codificarJustificacion(pJustificacion):
    """
    Funcionamiento: Encargado de codificar la justificacion
    Entradas:pJustificacion(str) tipo de justificacion
    Salida: NA
    """
    listaRazones=["Su peso baj&oacute; a menos de 50 kgms", "Ha recibido un trasplante de &oacutergano;.",
"Enfermedades como: tuberculosis, c&aacutencer; o cualquier enfermedad coronaria.", "Es adicto a alg&uacuten; tipo de droga.",
"Padeci&oacute; hepatitis B o C.","Has padecido de mal de Chagas."]
    return listaRazones[pJustificacion-1]
def generarAQuienDonar(pSangre):
    """
    Funcionamiento: Encargado de generar el reporte 6
    Entradas:pSangre(str) tipo de sangre
    Salida: NA
    """
    donar={"O-":["O-","O+","A-","A+","B-","B+","AB-","AB+"],"O+":["O+","A+","B+","AB+"],"A-":["A-","A+","AB-","AB+"],"A+":["A+","AB+"],"B-":["B-","B+","AB-","AB+"],"B+":["B+","AB+"],"AB-":["AB-","AB+"],"AB+":["AB+"]}
    try:
        donantes = leeDonante("donantes")
        listaDonantes=[]
        for donante in donantes:
            if donante[8]!=0:
                if donante[2] in donar[pSangre]:
                    listaDonantes.append(donante)
        for donante in range(len(listaDonantes)):
            if re.search("[áéíóúÁÉÍÓÚäëïöüÄËÏÖÜñ]",listaDonantes[donante][0])!=None:
                listaDonantes[donante][0]=codificador(listaDonantes[donante][0])
            if re.search("[áéíóúÁÉÍÓÚäëïöüÄËÏÖÜñ]",listaDonantes[donante][6])!=None:
                listaDonantes[donante][6]=codificador(listaDonantes[donante][6])
        return generarReporteAQuienDonar(listaDonantes,pSangre)
    except:
        return False
def generarReporteAQuienDonar(pLista,pSangre):
    """
    Funcionamiento: guarda una lista a la memoria secundaria y crear el HTML
    Entradas: 
    -pLista(lista) que se va a guardar en memoria secundaria
    -pSangre(str) tipo de sangre
    Salida: NA
    """
    try:
        escritura=open("DonadoreDe"+pSangre+".html","w")
        escritura.write("<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>Donadores que pueden recibir el tipo de sangre"+pSangre+" </title>\n\t\t<meta charset=\"UTF-8\">\n\t</head>\n<style type=\"text/css\">\n\ttable, th, td{\n\t\tborder: 1px solid black;\n\t\tborder-collapse: collapse;\n\t}\n</style>")
        escritura.write("\n\t<body>\n\t\t<center>\n\t\t\t<h1>Donadores que pueden recibir sangre </h1>\n\t\t\t<h2>Fecha y hora: "+str(datetime.datetime.now())[:-7]+"</h2>\n\t\t\t<table style=\"width: 100%\">")
        escritura.write("\n\t\t\t\t<tr>\n\t\t\t\t\t<th>C&eacute;dula</th>\n\t\t\t\t\t<th>Nombre completo</th>\n\t\t\t\t\t<th>Sangre</th>\n\t\t\t\t\t<th>Tel&eacute;fono</th>\n\t\t\t\t\t<th>Correo</th>\n\t\t\t\t</tr>")
        for donante in pLista:
            escritura.write("\n\t\t\t\t<tr>\n\t\t\t\t\t<td>"+donante[1]+"</td>\n\t\t\t\t\t<td>"+donante[0]+"</td>\n\t\t\t\t\t<td>"+donante[2]+"</td>\n\t\t\t\t\t<td>"+donante[7]+"</td>\n\t\t\t\t\t<td>"+donante[6]+"</td>\n\t\t\t\t</tr>")
        escritura.write("\n\t\t\t</table>\n\t\t</center>\n\t</body>\n</html>")
        escritura.close()
        return True
    except:
        return False
def deQuienRecibe(pSangre):
    """
    Funcionamiento: Encargado de generar el reporte 7
    Entradas:pSangre(str) tipo de sangre
    Salida: NA
    """
    recibe={"O-":["O-"],"O+":["O+","O-"],"A-":["O-","A-"],"A+":["O-","O+","A-","A+"],"B-":["B-","O-"],"B+":["O-","O+","B-","B+"],"AB-":["O-","A-","B-","AB-"],"AB+":["O-","O+","A-","A+","B-","B+","AB-","AB+"]}
    try:
        donantes = leeDonante("donantes")
        listaDonantes=[]
        for donante in donantes:
            if donante[8]!=0:
                if donante[2] in recibe[pSangre]:
                    listaDonantes.append(donante)
        for donante in range(len(listaDonantes)):
            if re.search("[áéíóúÁÉÍÓÚäëïöüÄËÏÖÜñ]",listaDonantes[donante][0])!=None:
                listaDonantes[donante][0]=codificador(listaDonantes[donante][0])
            if re.search("[áéíóúÁÉÍÓÚäëïöüÄËÏÖÜñ]",listaDonantes[donante][6])!=None:
                listaDonantes[donante][6]=codificador(listaDonantes[donante][6])
        return generarReporteQuienRecibe(listaDonantes,pSangre)
    except:
        return False
def generarReporteQuienRecibe(pLista,pSangre):
    """
    Funcionamiento: guarda una lista a la memoria secundaria y crear el HTML
    Entradas: 
    -pLista(lista) lista que se va a guardar
    pSangre(str) tipo de sangre
    Salida: NA
    """
    try:
        escritura=open("DonadoresPara"+pSangre+".html","w")
        escritura.write("<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>Donadores que pueden donarle al tipo de sangre "+pSangre+"</title>\n\t\t<meta charset=\"UTF-8\">\n\t</head>\n<style type=\"text/css\">\n\ttable, th, td{\n\t\tborder: 1px solid black;\n\t\tborder-collapse: collapse;\n\t}\n</style>")
        escritura.write("\n\t<body>\n\t\t<center>\n\t\t\t<h1>Donantes mujeres de sangre tipo O-</h1>\n\t\t\t<h2>Fecha y hora: "+str(datetime.datetime.now())[:-7]+"</h2>\n\t\t\t<table style=\"width: 100%\">")
        escritura.write("\n\t\t\t\t<tr>\n\t\t\t\t\t<th>C&eacute;dula</th>\n\t\t\t\t\t<th>Nombre completo</th>\n\t\t\t\t\t<th>Tipo de sangre</th>\n\t\t\t\t\t<th>Tel&eacute;fono</th>\n\t\t\t\t\t<th>Correo</th>\n\t\t\t\t</tr>")
        for donante in pLista:
            escritura.write("\n\t\t\t\t<tr>\n\t\t\t\t\t<td>"+donante[1]+"</td>\n\t\t\t\t\t<td>"+donante[0]+"</td>\n\t\t\t\t\t<td>"+donante[2]+"</td>\n\t\t\t\t\t<td>"+donante[7]+"</td>\n\t\t\t\t\t<td>"+donante[6]+"</td>\n\t\t\t\t</tr>")
        escritura.write("\n\t\t\t</table>\n\t\t</center>\n\t</body>\n</html>")
        escritura.close()
        return True
    except:
        return False   