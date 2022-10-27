from pydoc import describe

class Vehicle:
    def __init__(self,plate,description,chasis,driverName):
        self.__plate = plate
        self.__description = description
        self.__chasis = chasis
        self.__driverName = driverName
        self.__odometer = {}
        self.__totalKms = 0
        self.__history = ""

    def getPlate(self):
        self.__plate

    def getDescription(self):
        self.__description

    def getChasis(self):
        self.__chasis

    def getDriver(self):
        self.__driverName

    def getOdometer(self):
        self.__odometer 

    def getKilometers(self):
        self.__totalKms 

    def getHistory(self):
        self.__history 

    def addOdometer(self,date,fromCity,toCity,kms):
        self.__odometer[date] = (fromCity,toCity,kms)
    
    def confirmOdometer(self,date):
        detailOdo = self.__odometer.pop(date)
        self.__history += str(detailOdo[0])+"-"+str(detailOdo[1])+"-"+str(detailOdo[2]+"\n")
        self.__totalKms += detailOdo[2]
        
