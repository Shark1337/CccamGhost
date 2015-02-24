import unshortenit


class urllo():

    def __init__(self):

        ################################################################

        GoldenSat,status = unshortenit.unshorten('http://adf.ly/vdYeT')

        GoldenSat = GoldenSat.replace("http://","")

        GoldenSat = GoldenSat.split("/")

        self.host = str(GoldenSat[0])

        self.path = str("/"+GoldenSat[1]+"/"+GoldenSat[2])

        ################################################################

        CallShareRedCam,sratus = unshortenit.unshorten('http://adf.ly/rRGca')

        CallShareRedCam = CallShareRedCam.replace("http://","")

        CallShareRedCam = CallShareRedCam.split("/")

        self.HostCallShareRedCam = str(CallShareRedCam[0])

        self.PathCallShareRedCam = str("/"+CallShareRedCam[1]+"/"+CallShareRedCam[2])

