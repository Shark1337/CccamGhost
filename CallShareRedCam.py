mport httplib,urllib,urllo
import VariablesGlobales



class CallShareRedCam:
    """Clase que se encarga de sacar la linea de 48h del server especifico."""

    def __init__(self):
        self.X = VariablesGlobales.VariablesGlobales()
        self.B = urllo.urllo()


    def sacarLineaCallShareRedCam(self):

        connection = httplib.HTTPConnection(self.B.HostCallShareRedCam)
        parametros = urllib.urlencode({"user":"84.194."+self.X.RandomA+"."+self.X.RandomB,"pass":self.X.PASS})
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept":"text/plain"}
        connection.request("POST", self.B.PathCallShareRedCam, parametros, headers)
        response = connection.getresponse()
        LINEA = response.read()
        connection.close()
        return LINEA

    def remplazar(self,Posicion):
        archi=open(self.X.RutaArchTemp,'r')
        i=0
        LineaFinal = ""
        for LINEA in archi:
            if i == Posicion:
                LINEA = LINEA.replace('line-height: 1; <b>',"")
                a = LINEA.find(' </b> and expires on')
                LINEA = LINEA[:a]
                LINEA = LINEA.replace('<b>',"")
                LineaFinal = LINEA + "\n"
            i += 1

        archi.close()
        return LineaFinal
