from xmlrpc.client import DateTime
from vehicle import Vehicle
import requests

class Controlllervehicle():
    def __init__(self):
        self.__vehicles = {} #Key -> Plate, Value -> Vehicle

    def addVehicle(self,plate,description,chasis,driverName):
        if plate in self.__vehicles:
            return False
        self.__vehicles[plate] = Vehicle(plate,description,chasis,driverName)
        return True

    def delVehicle(self,plate):
        if plate in self.__vehicles:
            self.__vehicles.pop(plate) # del self.__vehicles[plate]
            return True
        return False

    def totalVehicles(self):
        return len(self.__vehicles)

    def getDistance(source, dest):
        url = "https://distanceto.p.rapidapi.com/get"

        querystring = {"route":"[{\"t\":\""+source+"\",\"c\":\"ES\"},{\"t\":\""+dest+"\",\"c\":\"ES\"}]","car":"true"}

        headers = {
            'x-rapidapi-host': "distanceto.p.rapidapi.com",
            'x-rapidapi-key': "498beeb34fmsh7558841455add94p17d283jsn987de2c3f201"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        if response.status_code == 200:
            data = response.json()
            meters = float(data["steps"][0]["distance"]["car"]["distance"])

    def addOdometer(self,plate,fromCity,toCity,date):
        if (plate not in self.__vehicles):
            return False
        kms = self.getDistance(fromCity,toCity)
        vehicle = self.__vehicles[plate]
        vehicle.addOdometer(date,fromCity,toCity,kms)
        return True
    
    def getVehicles(self):
        return self.__vehicles

    def confirmOdometer(self,plate,date):
        if (plate not in self.__vehicles):
            return False
        vehicle = self.__vehicles[plate]
        if date not in vehicle.getOdometer():
            return False
        vehicle.confirmOdometer(date)
        return True