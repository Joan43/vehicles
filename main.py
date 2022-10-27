from controllervehicle import Controlllervehicle

controller = Controlllervehicle()

def menu():
    print("Currently there are,", 0, "vehicles registred!")
    print("1.- Add a vehicle.")
    print("2.- Delete vehicle.")
    print("3.- Add a odometer.")
    print("4.- Confirm ofometer.")
    print("5.- List vehicle.")
    print("6.- Exite.")

def readPlate():
    plate = ""
    while True:
        plate = input("Enter the plate: ")
        if (len(plate) == 7):
            numPart = plate[0:4]
            lettersPart = plate[4:]
            if numPart.isdigit():
                if lettersPart.isalpha():
                    break
        print("Error entring the plate!")
    return plate
print("Vehicle deleted!")

def addVehicle():
    plate = readPlate()
    description = input("Enter description: ")
    while True:
        chasis = input("Enter chasis (17 characters): ")
        if len(chasis) == 17:
            break
        print("Error entring the chasis!")
    driver = input("Enter the driver name: ")
    if controller.addVehicle(plate,description,chasis,driver):
        print("Vehicle add successfuly.")
    else:
        print("Error adding the vehicle. Plate alredy exist!!")

def delVehicle():
    plate = readPlate()
    if controller.delVehicle(plate):
        print("Vehicle deleted!")
    else:
        print("Error vehicle deleted!")

def addOdometer():
    plate = readPlate()
    fromCity = input("From: ")
    toCity = input("To: ")
    date = input("Date: ")
    if controller.addOdometer(plate,fromCity,toCity,date):
        print("Odometer added sucessfuly!")
    else:
        print("Error adding the odometer!")

def listVehicle():
    vehicles = controller.getVehicles()
    for plate,vehicle in vehicles.items():
        print("Plate: ",vehicle.getPlate())
        print("Description: ",vehicle.getDescription())
        print("Chasis: ",vehicle.getChasis())
        print("Driver: ",vehicle.getDriver())
        print("Unconfirmed odometer: ")
        for date,odometer in vehicle.getOdometer().items():
            print("\t",date," - ",odometer[0]," - ",odometer[1]," - ",odometer[2])
        print("Kilometers: ",vehicle.getKilometers())
        print("History: ",vehicle.getHistory())

def confirmOdometer():
    plate = readPlate()
    date = input("Date: ")
    if controller.confirmOdometer(plate,date):
        print("Odometer confirmed!!")
    else:
        print("Error odometer!!")

while True:
    menu()
    option = int(input("Chose option: "))
    if option == 1:
        addVehicle()
    if option == 2:
        delVehicle()
    if option == 3:
        addOdometer()
    if option == 4:
        confirmOdometer()
    if option == 5:
        listVehicle()