import hacksat,Linea24,callshare,goldensat,kadersat,CallShareRedCam,Lycccam24

#--------------------------------------------------------------#


RutaCCcam = 'CCcam.cfg' #Cambiar 'CCcam.cfg' por la ruta donde esta el CCcam
RutaTemp = 'temp'

#--------------------------------------------------------------#

def creaciontxt():
    archi=open('temp','w')
    archi.close()

def escribir(data):
    archi=open('temp','a')
    archi.write(data)
    archi.close()

def BorrarLineasAntiguas():
    global RutaCCcam
    archi = open(RutaCCcam,'r')
    lineas = archi.readlines()
    archi.close()
    archi = open(RutaCCcam,'w')
    for linea in lineas:
        if linea.find('C:') == -1:
            archi.write(linea)

def sacarLinea(datos):
    creaciontxt()
    escribir(datos)
    

def escribirLineaenCCcam(Linea):
    
    global LineaEx,RutaCCcam
    archi = open(RutaCCcam,'a')
    archi.write(Linea)
    archi.close()


#--------------------------------------------------------------#
#Borrar Lineas anteriores
BorrarLineasAntiguas()



# Linea Lycccam24
L24 = Lycccam24.Linea24()
sacarLinea(L24.sacarLinea("http://www.mycccam24.com/redirect.php"))
Linea = L24.remplazar(68)
escribirLineaenCCcam(Linea)

# Linea Lycccam24
L24 = Lycccam24.Linea24()
sacarLinea(L24.sacarLinea("http://www.mycccam24.com/redirect1.php"))
Linea = L24.remplazar(68)
escribirLineaenCCcam(Linea)

# #Linea 24H3
L24 = Linea24.Linea24()
sacarLinea(L24.sacarLinea("http://mhrach.zapto.org/cccam/redirect.php"))
Linea = L24.remplazar(85)
escribirLineaenCCcam(Linea)

# #Linea 24H3
L24 = Linea24.Linea24()
sacarLinea(L24.sacarLinea("http://mhrach.zapto.org/cccam/redirect1.php"))
Linea = L24.remplazar(85)
escribirLineaenCCcam(Linea)


# #Linea 24H3
L24 = Linea24.Linea24()
sacarLinea(L24.sacarLinea("http://mhrach.zapto.org/cccam/redirect2.php"))
Linea = L24.remplazar(85)
escribirLineaenCCcam(Linea)

#Linea 24HB
L24 = Linea24.Linea24()
sacarLinea(L24.sacarLinea("http://mhrach.zapto.org/cccam/redirect3.php"))
Linea = L24.remplazar(85)
escribirLineaenCCcam(Linea)

#Linea Hacksat
datos= hacksat.Hacksat()
sacarLinea(datos.sacarLineaHacksat())
Linea = datos.remplazar(181)
escribirLineaenCCcam(Linea)

#Linea Callshare
datos=callshare.Callshare()
sacarLinea(datos.sacarLineaCallshare())
Linea = datos.remplazar(315)
escribirLineaenCCcam(Linea)

#Linea Kader-sat
datos=kadersat.Kadersat()
sacarLinea(datos.sacarLineaKadersat())
Linea = datos.remplazar(90)
escribirLineaenCCcam(Linea)

#Linea CallShareRedCam
datos=CallShareRedCam.CallShareRedCam()
sacarLinea(datos.sacarLineaCallShareRedCam())
Linea = datos.remplazar(315)
escribirLineaenCCcam(Linea)
