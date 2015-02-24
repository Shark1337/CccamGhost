import urllib2
import VariablesGlobales



class Linea24:
    """Clase que saca la linea de 24h"""


    def __init__(self):
        self.X = VariablesGlobales.VariablesGlobales()

    def sacarLinea(self,Direccion):
        h = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0"}
        cookie_h = urllib2.HTTPCookieProcessor()
        opener = urllib2.build_opener(cookie_h)
        urllib2.install_opener(opener)
        f = urllib2.urlopen(Direccion)
        LINEA = f.read()
        return LINEA

    def remplazar(self,Posicion):
        archi=open(self.X.RutaArchTemp,'r')
        i=0
        LineaFinal = ""
        for LINEA in archi:
            if i == Posicion:
                LINEA = LINEA.replace('</body><h3> <br> Your Free CCcam line is <br> <FONT COLOR="#75D246"> ',"")
                LINEA = LINEA.replace('</body><h3> <br> Your Free CCcam line is :<br> <FONT COLOR="#75D246"> ',"")
                a = LINEA.find('</FONT>')
                LINEA = LINEA[:a]
                LineaFinal = LINEA + "\n"
            i += 1

        archi.close()
        return LineaFinal
