import httplib,urllib
import VariablesGlobales

class Kadersat:
    """Clase que se encarga de sacar la linea de 48h del server especifico."""

    def __init__(self):
        self.X = VariablesGlobales.VariablesGlobales()


    def sacarLineaKadersat(self):
        connection = httplib.HTTPConnection("kader-sat.ddns.net")
        parametros = urllib.urlencode({"user":"84.194."+self.X.RandomA+"."+self.X.RandomB,"pass":"kaderserver","submit":"Activate%21"})
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept":"text/plain"}
        connection.request("POST", "/index.php", parametros, headers)
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
                LINEA = LINEA.replace('</body><br><h3>Your Free CCcam line is <br><br> ',"")
                a = LINEA.find(':|:')
                LINEA = LINEA[:a]
                LINEA = LINEA.replace('<b>',"")
                LineaFinal = LINEA + "\n"
            i += 1

        archi.close()
        return LineaFinal
