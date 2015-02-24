import httplib,urllib,urllo
import VariablesGlobales


class Goldensat:
    """Clase que se encarga de sacar la linea de 48h del server especifico."""

    def __init__(self):
        self.X = VariablesGlobales.VariablesGlobales()
        self.A = urllo.urllo()


    def sacarLineaGoldesat(self):
        host = self.A.host
        path = self.A.path
        connection = httplib.HTTPConnection(host)
        parametros = urllib.urlencode({"user":"84.194."+self.X.RandomA+"."+self.X.RandomB,"pass":self.X.PASS,"submit":"Activate"})
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept":"text/plain"}
        connection.request("POST",path, parametros, headers)
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
                LINEA = LINEA.replace('<b>',"")
                LINEA = LINEA.replace('</b> and expires on 21-02-2015 ',"")
                LineaFinal = LINEA + "\n"
            i += 1

        archi.close()
        return LineaFinal
