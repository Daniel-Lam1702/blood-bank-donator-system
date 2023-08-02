#Elaborado por Daniel Eduardo Lam He
#Fecha de creacion: 10/05/2021 10:00 am
#Última fecha de modificación: 17/05/2021 4:25 pm
#Versión:3.9.2
#Llamada de librerias
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re
import datetime
from tkinter.font import Font
from memoriaSecundaria import*
from funciones import*
from archivos import *
#Se genera la ventana principal
ventanaPrincipal = Tk()
ventanaPrincipal.title("Ventana Principal")
ventanaPrincipal.geometry("1080x1080")
#Definicion de funciones
#------------------------------------Insertar Donador-----------------------------------
def registrarDonadorAux(pDonador,pVentana):
    try:
        cantidadDias=[31,29,31,30,31,30,31,31,30,31,30,31]
        if re.match("[1-9]\-\d{4}\-\d{4}",pDonador[1]) == None:
            messagebox.showerror("Error","Debe ingresar una cédula válida",parent=pVentana)
            return False
        elif pDonador[0] == "":
            messagebox.showerror("Error","Debe ingresar un nombre",parent=pVentana)
            return False        
        elif re.match("\d{2}/\d{2}/\d{4}",pDonador[4]) == None:
            messagebox.showerror("Error","Debe ingresar una fecha de nacimiento válido",parent=pVentana)
            return False
        elif int(pDonador[4][3:5])>12:
            messagebox.showerror("Error","Debe ingresar un mes válido en la fecha de nacimiento",parent=pVentana)
            return False  
        elif int(pDonador[4][:2])>cantidadDias[int(pDonador[4][3:5])-1]:
            messagebox.showerror("Error","Debe ingresar un día válido en la fecha de nacimiento",parent=pVentana)
            return False        
        elif re.match("^\d+$",pDonador[5]) == None:
            messagebox.showerror("Error","Debe ingresar un peso válido",parent=pVentana)
            return False     
        elif re.match("\d{4}-\d{4}",pDonador[7]) == None:
            messagebox.showerror("Error","Debe ingresar un teléfono válido",parent=pVentana)
            return False
        elif re.match("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[\w]+([\.][\w]+|[\.][\w]+[\.][\w]+)$",pDonador[6]) == None:
            messagebox.showerror("Error","Debe ingresar un correo válido",parent=pVentana)
            return False  
        for donante in leeDonante("donantes"):
            if pDonador[1] in donante:
                messagebox.showerror("Error","Usted ya se encuentra registrad@",parent=pVentana)
                return False      
        return True
    except:
        messagebox.showerror("Error","Se generó un error",parent=pVentana)
        return False 
def verSiMayor(fechaNac):
    fechaActual=datetime.datetime.now()
    if fechaActual.year-int(fechaNac[6:])>18:
        return True
    elif fechaActual.year-int(fechaNac[6:])==18:
        if fechaActual.month >= int(fechaNac[3:5]):
            return True         
    return False
def adultoMayor(fechaNac):
    fechaActual=datetime.datetime.now()
    if fechaActual.year-int(fechaNac[6:])<65:
        return True
    elif fechaActual.year-int(fechaNac[6:])==65:
        if fechaActual.month >= int(fechaNac[3:5]):
            return True         
    return False
def verPeso(pPeso):
    if pPeso<=50 or pPeso>=120:
        return False
    return True
def mostrarLugares(pListaHospital):
    hospitales=""
    if len(pListaHospital) == 1:
        return pListaHospital[0]
    for j in range(len(pListaHospital)):
        if j+1 != len(pListaHospital):
            hospitales +=" "+pListaHospital[j]+","
        else:
            hospitales=hospitales[:-1]+" y "+pListaHospital[j]+"."
    return hospitales
def indicarLugar(pProvincia):
    nacionalizaciones = {"1":"San José","2":"Alajuela","3":"Cartago","4":"Heredia","5":"Guanacaste","6":"Puntarenas",
    "7":"Limón","8":"Nacionalizado o naturalizado","9":"Partida especial de nacimientos"}
    lugar = leeLugar("lugares")
    if pProvincia == "8":
        return "2. Dado que usted está "+nacionalizaciones[pProvincia]+", usted podría donar en:\n" + mostrarLugares(lugar[nacionalizaciones["1"]])
    elif pProvincia == "9":
        return "2. Dado que usted pertenece a una "+nacionalizaciones[pProvincia]+", usted podría donar en:\n" + mostrarLugares(lugar[nacionalizaciones["1"]])
    else:
        return "2. Dado que usted nació en la provincia de "+nacionalizaciones[pProvincia]+", usted podría donar en:\n" + mostrarLugares(lugar[nacionalizaciones[pProvincia]])
def indicarSangre(pSangre):
    sangres = {"A+":"sangre entera y plaquetas.",
    "A-":"sangre entera y glóbulos rojos dobles.",
    "B+":"sangre entera y de glóbulos rojos dobles.",
    "B-":"sangre entera o plaquetas.",
    "O+":"glóbulos rojos dobles y sangre entera.",
    "O-":"glóbulos rojos dobles y sangre entera.",
    "AB+":"plaquetas y plasma.",
    "AB-":"plaquetas y plasma."}  
    return sangres[pSangre]  
def insercionInicial(pDonador):
    ventanaInsercion = Toplevel()
    ventanaInsercion.title("Información")
    ventanaInsercion.geometry("720x720")
    Label(ventanaInsercion,text="Información sobre el donante", font=Font(weight="bold",size=12)).grid(row=0,column=0,sticky="nwse")
    if verSiMayor(pDonador[4]) and adultoMayor(pDonador[4]):
        Label(ventanaInsercion,text="1. Dado su fecha de nacimiento usted ya puede ser donador.",font=Font(size=11)).grid(row=1,column=0,sticky="nwse")
    else:
        if verSiMayor(pDonador[4])==False:
            Label(ventanaInsercion,text="1. Dado su fecha de nacimiento usted aún no puede ser donador.",font=Font(size=11)).grid(row=1,column=0,sticky="nwse")
        else:
            Label(ventanaInsercion,text="1. Dado su fecha de nacimiento usted ya no puede ser donador.",font=Font(size=11)).grid(row=1,column=0,sticky="nwse")
    Label(ventanaInsercion,text=indicarLugar(pDonador[1][0]),font=Font(size=11)).grid(row=2,column=0,sticky="nwse")
    if verPeso(int(pDonador[5])):
        Label(ventanaInsercion,text="3. Usted posee un peso adecuado, correcto para ser donador de sangre.",font=Font(size=11)).grid(row=3,column=0,sticky="nwse")
    else:
        Label(ventanaInsercion,text="3. Usted debe pesar más de 50kgms y menos de 120kgms para poder ser donador.",font=Font(size=11)).grid(row=3,column=0,sticky="nwse")
    Label(ventanaInsercion,text="4. Dado su tipo de sangre y RH usted puede donar: "+indicarSangre(pDonador[2]),font=Font(size=11)).grid(row=4,column=0,sticky="nwse")
    Button(ventanaInsercion,text="Salir",command=lambda:eliminarVentana(ventanaInsercion),font=Font(size=13),padx=50,pady=25, activebackground="lightblue").grid(row=5,column=0)
#Organizar los widgets 
    for i in range(6):
        Grid.rowconfigure(ventanaInsercion, i, weight = 1)
    Grid.columnconfigure(ventanaInsercion, 0, weight = 1)
    return 
def opcionRegistrarDonador(pDonador,pVentana):
    if registrarDonadorAux(pDonador,pVentana):
        if verSiMayor(pDonador[4]) and verPeso(int(pDonador[5])) and adultoMayor(pDonador[4]):
            registrarDonador(pDonador)
        insercionInicial(pDonador)
        eliminarVentana(pVentana)
    return 
def limpiar(pLista):
    for i in pLista:
        i.delete(0,END)
    return
def eliminarVentana(ventana):
    ventana.destroy()
    return
#Ventana principal del boton 1 
def boton1():
    ventana_1 = Toplevel()
    ventana_1.title("Insertar donador")
    ventana_1.geometry("1080x1080")
#Título
    Label(ventana_1,text="Inserte los datos del donador", font=Font(weight="bold",size=12)).grid(row = 0, column = 0, columnspan=2,sticky = "nswe")
#Insertar cédula
    Label(ventana_1,text="Numero de cédula (#-####-####)").grid(row = 1, column = 0,sticky = "e")
    cedula = Entry(ventana_1,width = 40)
    cedula.grid(row = 1, column = 1, sticky="w")
#Insertar nombre
    Label(ventana_1,text="Nombre Completo").grid(row = 2, column = 0, sticky = "e")
    nombre = Entry(ventana_1,width = 40)
    nombre.grid(row = 2, column = 1, sticky="w")
#Insertar fecha de nacimiento
    Label(ventana_1,text="Fecha de nacimiento (DD/MM/AAAA)").grid(row = 3, column = 0, sticky = "e")
    fecha = Entry(ventana_1,width = 40)
    fecha.grid(row = 3, column = 1, sticky="w")
#Insertar el tipo de sangre
    Label(ventana_1,text="Tipo de sangre").grid(row = 4, column = 0, sticky ="e")    
    sangres = ["O+","O-","A+","A-","B+","B-","AB+","AB-"]
    sangre = ttk.Combobox(ventana_1,value = sangres, state="readonly")
    sangre.current(0)
    sangre.grid(row = 4, column = 1, sticky="w")
#Escoger sexo
    sexo = BooleanVar(ventana_1,value=True)
    Radiobutton(ventana_1, text="Femenino", variable=sexo, value=False).grid(row = 6, column=1, sticky="w")
    Radiobutton(ventana_1, text="Masculino", variable=sexo, value=True).grid(row = 5, column=1, sticky="w")
    Label(ventana_1,text="Sexo").grid(row = 5, rowspan=2, column = 0,sticky = "e")
#Insertar peso
    Label(ventana_1,text="Peso(Kg)").grid(row = 7, column = 0, sticky="e")
    peso = Entry(ventana_1,width = 40)
    peso.grid(row = 7, column = 1,sticky="w")
#Insertar telefono
    Label(ventana_1,text="Número de teléfono (####-####)").grid(row = 8, column = 0, sticky = "e")
    telefono = Entry(ventana_1,width = 40)
    telefono.grid(row = 8, column = 1,sticky="w")
#Insertar correo
    Label(ventana_1,text="Correo").grid(row = 9, column = 0, sticky = "e")
    correo = Entry(ventana_1,width = 40)
    correo.grid(row = 9, column = 1,sticky="w")
#Botones
    Button(ventana_1,text = "Registrar", activebackground="lightblue",command = lambda: opcionRegistrarDonador([nombre.get(),cedula.get(),sangre.get(),sexo.get(),fecha.get(),peso.get(),correo.get(),telefono.get()],ventana_1)).grid(row = 10,column=0,columnspan=2,sticky = "nwse")
    Button(ventana_1,text = "Limpiar", activebackground="lightblue",command = lambda : limpiar([nombre,cedula,fecha,peso,telefono,correo])).grid(row = 11,column=0,columnspan=2,sticky = "nwse")
    Button(ventana_1,text = "Regresar", activebackground="lightblue",command = lambda : eliminarVentana(ventana_1)).grid(row = 12,column=0,columnspan=2,sticky = "nwse")
#Organizar los widgets 
    for i in range(13):
        Grid.rowconfigure(ventana_1, i, weight = 1)
    Grid.columnconfigure(ventana_1, 0, weight = 1)
    Grid.columnconfigure(ventana_1, 1, weight = 1)
    return 
def boton2():
    ventana_2 = Tk()
    ventana_2.title("Generar donadores")
    return 
def boton3():
    ventana_3 = Tk()
    ventana_3.title("Actualizar datos del donador")
    return 
#-------------------------------Eliminar Donador------------------------------
def eliminarDonadorAux(pCedula,pVentana):
    valorDeVerdad=False
    if re.match("[1-9]\-\d{4}\-\d{4}",pCedula) == None:
        messagebox.showerror("Error","Debe ingresar una cédula válida",parent = pVentana)
        return False
    for donante in leeDonante("donantes"):
        if pCedula in donante:
            valorDeVerdad=True
            break
    if valorDeVerdad==False:
        messagebox.showerror("Error","La persona con el número de cédula: "+pCedula+" no está registrado en la base de datos del Banco de Sangre aún.",parent = pVentana)
        return False    
    return True 
def antesEliminarDonador(pCedula,pJustificacion,pVentana4,pVentanaJust):
    respuesta = messagebox.askyesno("Eliminar donador","¿Desea eliminar al donador ingresado?",parent = pVentanaJust)
    if respuesta:
        eliminarDonador(pCedula,pJustificacion)
        messagebox.showinfo("Eliminar donador","Donador eliminado satisfactoriamente",parent = pVentanaJust)
        pVentanaJust.destroy()
        pVentana4.destroy()
    else:
        messagebox.showinfo("Eliminar donador","Donador NO eliminado",parent = pVentanaJust)        
    return    
def pedirJustificacion(pCedula,pVentana4):
    ventanaJust = Toplevel()
    ventanaJust.title("Eliminar donador")
    ventanaJust.geometry("720x720")
    listaRazones=["Su peso bajó a menos de 50 kgms", "Ha recibido un trasplante de órgano.",
"Enfermedades como: tuberculosis, cáncer o cualquier enfermedad coronaria.", "Es adicto a algún tipo de droga.",
"Padeció hepatitis B o C.","Has padecido de mal de Chagas."]
#Titulo
    Label(ventanaJust,text="Escoja la razón por la cual desea eliminar el donador", font=Font(weight="bold",size=12)).grid(row = 0, column = 0, columnspan=2,sticky = "nswe")
#Opcion unica
    justificacion = IntVar(ventanaJust,value=1)
    for i in range(1,7):
        Radiobutton(ventanaJust, text=listaRazones[i-1], variable=justificacion, value=i).grid(row = i, column=0)
#Definicion de botones    
    Button(ventanaJust,text = "Eliminar", activebackground="lightblue",command = lambda : antesEliminarDonador(pCedula,justificacion.get(),pVentana4,ventanaJust)).grid(row = 7,column=0,sticky = "nwse")
    Button(ventanaJust,text = "Regresar", activebackground="lightblue",command = lambda : eliminarVentana(ventanaJust)).grid(row = 8,column=0,sticky = "nwse")
#Organizar los widgets    
    for i in range(9):
        Grid.rowconfigure(ventanaJust, i, weight = 1)
    Grid.columnconfigure(ventanaJust, 0, weight = 1)    
    return
def opcionEliminarDonador(pCedula,pVentana):
    if eliminarDonadorAux(pCedula,pVentana):
        pedirJustificacion(pCedula,pVentana)
    return
"""Ventana principal del boton 4"""
def boton4():
    ventana_4 = Toplevel()
    ventana_4.title("Eliminar donador")
    ventana_4.geometry("720x720")
#Título
    Label(ventana_4,text="Inserte el número de cédula del donador que desea eliminar", font=Font(weight="bold",size=12)).grid(row = 0, column = 0, columnspan=2,sticky = "nswe")
#Insertar cédula
    Label(ventana_4,text="Numero de cédula (#-####-####)").grid(row = 1, column = 0,sticky = "nse")
    cedula = Entry(ventana_4,width = 40)
    cedula.grid(row = 1, column = 1, sticky="w")
#Definición de botones
    Button(ventana_4,text = "Eliminar", activebackground="lightblue",command = lambda: opcionEliminarDonador(cedula.get(),ventana_4),pady=30,padx=60).grid(row = 2,column=0,columnspan=2)
    Button(ventana_4,text = "Limpiar", activebackground="lightblue",command = lambda : limpiar([cedula]),pady=30,padx=60).grid(row = 3,column=0,columnspan=2)
    Button(ventana_4,text = "Regresar", activebackground="lightblue",command = lambda : eliminarVentana(ventana_4),pady=30,padx=60).grid(row = 4,column=0,columnspan=2)
#Organizacion de widgets
    for i in range(5):
        Grid.rowconfigure(ventana_4, i, weight = 1)
    Grid.columnconfigure(ventana_4, 0, weight = 1)
    Grid.columnconfigure(ventana_4, 1, weight = 1)
    return
def boton5():
    ventana_5 = Tk()
    ventana_5.title("Insertar lugar de donación según provincia")
    return
"""Reporte 1"""
def opcionReporteProvincia(pProvincia,pVentana):
    provincias = {"San José":"1","Alajuela":"2","Cartago":"3","Heredia":"4","Guanacaste":"5",
    "Puntarenas":"6","Limón":"7","Nacionalizado o naturalizado":"8","Partida especial de nacimientos":"9"}
    if generarListaDonantesProvincia(provincias[pProvincia],pProvincia):
        messagebox.showinfo("Donantes por provincia","Reporte creado satisfactoriamente",parent=pVentana)
    else:
        messagebox.showinfo("Donantes por provincia","Reporte no creado",parent=pVentana)
    return
def generarDonantesProvincia():
#Generación de la ventana
    ventanaDonantesProvincia = Toplevel()
    ventanaDonantesProvincia.title("Donantes por provincia")
    ventanaDonantesProvincia.geometry("720x720")
#Generación del título
    Label(ventanaDonantesProvincia,text="Donantes por provincia",font=Font(weight="bold",size=12)).grid(row = 0, column = 0,columnspan=2, sticky ="nswe")
#Creacion de la caja de selección
    Label(ventanaDonantesProvincia,text="Escoja la provincia").grid(row = 3, column = 0, sticky ="e")    
    provincias = ["San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón","Nacionalizado o naturalizado","Partida especial de nacimientos"]
    provincia = ttk.Combobox(ventanaDonantesProvincia,value = provincias, state="readonly",width=50)
    provincia.current(0)
    provincia.grid(row = 3, column = 1, sticky="w")
#Generación de botones
    Button(ventanaDonantesProvincia, text="Generar reporte", activebackground="lightblue", command= lambda: opcionReporteProvincia(provincia.get(),ventanaDonantesProvincia)).grid(row = 6, column = 0, columnspan=2, sticky ="nswe")
    Button(ventanaDonantesProvincia, text="Regresar", activebackground="lightblue", command = lambda : eliminarVentana(ventanaDonantesProvincia)).grid(row = 7, column = 0,columnspan=2, sticky ="nswe")
#Organizacion de widgets
    for i in range(8):
        Grid.rowconfigure(ventanaDonantesProvincia, i, weight = 1)
    Grid.columnconfigure(ventanaDonantesProvincia, 0, weight = 1)
    Grid.columnconfigure(ventanaDonantesProvincia, 1, weight = 1)
    return
"""Reporte 2"""
def validarEdad(pEdadInicial,pEdadFinal,pVentana):
    if re.match("^\d+$",pEdadInicial) == None:
        messagebox.showerror("Error","Debe ingresar una edad inicial válida",parent=pVentana)
        return False
    elif re.match("^\d+$",pEdadFinal) == None:
        messagebox.showerror("Error","Debe ingresar una edad final válida válida",parent=pVentana)
        return False
    elif int(pEdadInicial)>int(pEdadFinal):
        messagebox.showerror("Error","La edad inicial debe ser menor o igual a la final",parent=pVentana)
        return False        
    return True
def opcionGenerarDonantesEdad(pEdadInicial,pEdadFinal,pVentana):
    if validarEdad(pEdadInicial,pEdadFinal,pVentana):
        if generarListaDonantesEdad(int(pEdadInicial),int(pEdadFinal)):
            messagebox.showinfo("Donantes por rango de edad","Reporte creado satisfactoriamente",parent=pVentana)
        else:
            messagebox.showinfo("Donantes por rango de edad","Reporte no creado",parent=pVentana)
    return
def generarDonantesEdad():
#Generación de la ventana
    ventanaDonantesEdad = Toplevel()
    ventanaDonantesEdad.title("Donantes por rango de edad")
    ventanaDonantesEdad.geometry("720x720")
#Generación del título
    Label(ventanaDonantesEdad,text="Donantes por rango de edad",font=Font(weight="bold",size=12)).grid(row = 0, column = 0,columnspan=2, sticky ="nswe")
#Creacion de la caja de texto
    Label(ventanaDonantesEdad,text="Inserte el rango de edad en las cajas de texto").grid(row = 1, column = 0, columnspan = 2, sticky ="nswe")    
    Label(ventanaDonantesEdad,text="Edad inicial(##):").grid(row=3,column=0,sticky="e")
    edadInicial=Entry(ventanaDonantesEdad,width=25)
    edadInicial.grid(row=3,column=1,sticky="w")
    Label(ventanaDonantesEdad,text="Edad final(##):").grid(row=4,column=0,sticky="e")
    edadFinal=Entry(ventanaDonantesEdad,width=25)
    edadFinal.grid(row=4,column=1,sticky="w")
#Generación de botones
    Button(ventanaDonantesEdad, text="Generar reporte", activebackground="lightblue", command= lambda: opcionGenerarDonantesEdad(edadInicial.get(),edadFinal.get(),ventanaDonantesEdad)).grid(row = 7, column = 0, columnspan=2, sticky ="nswe")
    Button(ventanaDonantesEdad, text="Regresar", activebackground="lightblue", command = lambda : eliminarVentana(ventanaDonantesEdad)).grid(row = 8, column = 0,columnspan=2, sticky ="nswe")
#Organizacion de widgets
    for i in range(9):
        Grid.rowconfigure(ventanaDonantesEdad, i, weight = 1)
    Grid.columnconfigure(ventanaDonantesEdad, 0, weight = 1)
    Grid.columnconfigure(ventanaDonantesEdad, 1, weight = 1)
    return
"""Reporte 3"""
def opcionReporteSangre(pSangre,pVentana):
    if generarListaDonantesSangre(pSangre):
        messagebox.showinfo("Donantes por Sangre","Reporte creado satisfactoriamente",parent=pVentana)
    else:
        messagebox.showinfo("Donantes por Sangre","Reporte no creado",parent=pVentana)
    return
def generarDonantesSangre():
#Generación de la ventana
    ventanaDonantesSangre = Toplevel()
    ventanaDonantesSangre.title("Donantes por Sangre")
    ventanaDonantesSangre.geometry("720x720")
#Generación del título
    Label(ventanaDonantesSangre,text="Generar reporte de donantes por Sangre",font=Font(weight="bold",size=12)).grid(row = 0, column = 0,columnspan=2, sticky ="nswe")
#Creacion de la caja de selección
    Label(ventanaDonantesSangre,text="Escoja el tipo de sangre").grid(row = 3, column = 0, sticky ="e")    
    listaSangres = ["O+","O-","A+","A-","B+","B-","AB+","AB-"]
    sangre = ttk.Combobox(ventanaDonantesSangre,value = listaSangres, state="readonly")
    sangre.current(0)
    sangre.grid(row = 3, column = 1, sticky="w")
#Generación de botones
    Button(ventanaDonantesSangre, text="Generar reporte", activebackground="lightblue", command= lambda: opcionReporteSangre(sangre.get(),ventanaDonantesSangre)).grid(row = 6, column = 0, columnspan=2, sticky ="nswe")
    Button(ventanaDonantesSangre, text="Regresar", activebackground="lightblue", command = lambda : eliminarVentana(ventanaDonantesSangre)).grid(row = 7, column = 0,columnspan=2, sticky ="nswe")
#Organizacion de widgets
    for i in range(8):
        Grid.rowconfigure(ventanaDonantesSangre, i, weight = 1)
    Grid.columnconfigure(ventanaDonantesSangre, 0, weight = 1)
    Grid.columnconfigure(ventanaDonantesSangre, 1, weight = 1)
    return
"""Reporte 4"""
def opcionGenerarListaCompleta(pVentana):
    if generarListaCompleta():
        messagebox.showinfo("Donantes por provincia","Reporte creado satisfactoriamente",parent=pVentana)
    else:
        messagebox.showinfo("Donantes por provincia","Reporte no creado",parent=pVentana)
    return
"""Ventana principal del boton 6: Generar reportes"""
def boton6():
    ventana_6 = Toplevel()
    ventana_6.title("Reportes")
    ventana_6.geometry("720x720")
    Label(ventana_6,text="Escoja el tipo de reporte que desea generar",font=Font(weight="bold")).grid(row=0,column=0)
    Button(ventana_6,text="Donantes por provincia", activebackground="lightblue",command=generarDonantesProvincia,padx=60,pady=25).grid(row=1,column=0)
    Button(ventana_6,text="Donantes por rango de edad", activebackground="lightblue",command=generarDonantesEdad,padx=47,pady=25).grid(row=2,column=0)
    Button(ventana_6,text="Donantes por tipo de sangre", activebackground="lightblue",command=generarDonantesSangre,padx=47,pady=25).grid(row=3,column=0)
    Button(ventana_6,text="Lista completa de donadores", activebackground="lightblue",command= lambda: opcionGenerarListaCompleta(ventana_6),padx=47,pady=25).grid(row=4,column=0)
    Button(ventana_6,text = "Regresar", activebackground="lightblue",command = lambda : eliminarVentana(ventana_6),padx=100,pady=25).grid(row = 5,column=0)    
#Organizacion de widgets
    for i in range(6):
        Grid.rowconfigure(ventana_6, i, weight = 1)
    Grid.columnconfigure(ventana_6, 0, weight = 1)
    return
def boton7():
    respuesta = messagebox.askyesno("Salida","¿Desea salir?")
    if respuesta:
        messagebox.showinfo("Salir","Donar sangre, es donar vida")
        ventanaPrincipal.destroy()
    return
#Creacion de botones de la ventana principal
textoInicial=Label(ventanaPrincipal,text="Bienvenid@ al Banco de Sangre\n¿Qué desea realizar?",font=Font(weight="bold"),pady = 20).grid(row = 0,column = 0,sticky = "nsew")
Button(ventanaPrincipal, text="Insertar donador", command = boton1,pady = 25, padx = 105, activebackground="lightblue").grid(row = 1 ,column = 0)
Button(ventanaPrincipal, text="Generar donadores", command = boton2,pady = 25, padx = 100, activebackground="lightblue").grid(row = 2 ,column = 0)
Button(ventanaPrincipal, text="Actualizar datos del donador", command = boton3,pady = 25, padx = 75, activebackground="lightblue").grid(row = 3 ,column = 0)
Button(ventanaPrincipal, text="Eliminar donador", command = boton4,pady = 25, padx = 105, activebackground="lightblue").grid(row = 4 ,column = 0)
Button(ventanaPrincipal, text="Insertar lugar de donación según provincia", command = boton5,pady = 25, padx = 38, activebackground="lightblue").grid(row = 5 ,column = 0)
Button(ventanaPrincipal, text="Reportes", command = boton6,pady = 25, padx = 128, activebackground="lightblue").grid(row = 6 ,column = 0)
Button(ventanaPrincipal, text="Salir", command = boton7,pady = 25, padx = 140, activebackground="lightblue").grid(row = 7 ,column = 0)
#Configurar las columnas y filas
for i in range(8):
    Grid.rowconfigure(ventanaPrincipal, i, weight = 1)
Grid.columnconfigure(ventanaPrincipal, 0, weight = 1)
#Se abre la ventana
ventanaPrincipal.mainloop()