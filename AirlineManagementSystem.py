from aircraftmanager import AircraftManager
from FlightManger import FlightManager
from BookingManger import BookingManager
from passangerManager import PassagerManager
aircraftManager = AircraftManager()
flightManager = FlightManager(aircraftManager)
PassagerManager = PassagerManager()
BookingManager =BookingManager(flightManager,PassagerManager)

def mainMenu():
    print("Enter 0 to exit")
    print("Enter 1 to Manage Aircrafts")
    print("Enter 2 to Manage Flights")
    print("Enter 3 to Manage Bookings")
    print("Enter 4 to Manage passangers")

    
def showSubMenu(option):
    if option == "1":
        showManageAircraftsMenu()
        subOption=input()
        if subOption == "0":
            mainMenu()
        else:
            handleManageAircraftsAction(subOption)
    elif option == "2":
        showManageFlightMenu()
        subOption=input()
        if subOption == "0":
            mainMenu()
        else:
            handleManageFlightMenuAction(subOption)
    elif option == "3":
        showManageBookingsMenu()
        subOption = input()
        if subOption =="0":
            mainMenu()
        else:
            handleManageBookingsAction(subOption)
    elif option == "4":
        showManagePassangerMenu()
        subOption = input()
        if subOption == "0":
            mainMenu()
        else:
            handleManagePassangerAction(subOption)

def showManagePassangerMenu():
    print("Enter 0 to return to MainMenu")
    print("Enter 1 to List Passangers")
    print("Enter 2 to Create Passanger")
    print("Enter 3 to update passanger")
    print("Enter 4 to delete passanger")




def handleManagePassangerAction(action):
    if action == "1":
        PassagerManager.list()
    elif action == "2":
        name =input("Enter Name of Passanger? ")
        age =input("Enter Passanger age? ")
        PhoneNo = input("Enter passangers Phone number? ")
        Email= input("Enter Email?")
        Address= input("Enter Address?")
        PassagerManager.create(name,age,PhoneNo,Email,Address)
        print("Congrats!", name, "is a passanger on a flight")
    elif action == "3":
        name =input("Enter Name of Passanger? ")
        age =input("Enter Passanger age? ")
        PhoneNo = input("Enter passangers Phone number? ")
        Email= input("Enter Email?")
        Address= input("Enter Address?")
        PassagerManager.update(name,age,PhoneNo,Email,Address)
        print(PhoneNo,"updated")
    elif action == "4":
        PhoneNo = input("Enter passangers Phone number? ")
        PassagerManager.delete(PhoneNo)
        
    showSubMenu("4")



        
def showManageBookingsMenu():
    print("Enter 0 to return to MainMenu")
    print("Enter 1 to List Bookings")
    print("Enter 2 to Create Booking")
    print("Enter 3 to update Booking")
    print("Enter 4 to delete Booking")


def handleManageBookingsAction(action):
    if action == "1":
        BookingManager.list()
    elif action == "2":
        name =input("Enter name? ")
        SitNumber =input("Enter SiteNumber? ")
        Price = input("Enter price? ")
        TypeOfFlight = input("Enter Type Of Flight?")
        TimeOfFlight = input("Enter Time of flight?")
        destination = input("Enter destination?")
        avalFlight = input("Enter the Flight number")
        PhoneNo = input("Enter the Phone number")
        response =BookingManager.create(destination,TimeOfFlight,TypeOfFlight,SitNumber,name,Price,avalFlight,PhoneNo)
        if response :
            print("Congrats! Your Booking ",name," is created successfully")
        else:
            print("name",name," not available")
    elif action == "3":
        name = input("Enter name? ")                                      
        destination = input("Enter destination?")
        TimeOfFlight = input("Enter Type Of Flight?")
        TypeOfFlight = input("Enter Type Of Flight?")
        Price = input("Enter price? ")
        SitNumber = input("Enter SiteNumber? ")
        BookingManager.update(destination,TimeOfFlight,TypeOfFlight,Price,SitNumber,name)
        print(SitNumber,"updated")
    elif action == "4":
        SitNumber =input("Enter SiteNumber? ")
        BookingManager.delete(SitNumber)

    showSubMenu("3")




def handleManageFlightMenuAction(action):
    if action == "1":
        flightManager.list()
    elif action == "2":
        flightno =input("Enter Flight No? ")
        takeofftime =input("Enter takeoffTime? ")
        takepoint = input("Enter takepoint? ")
        registrationNo = input("Enter registartioNo ? ")
        destination = input("Enter your destination? ")
        landingtime = input("Enter landing time? ")
        price = input("Enter price?")
        response =flightManager.create(flightno,takeofftime,takepoint,registrationNo,destination,landingtime,price)
        if response :
            print("Congrats! Your Flight ",flightno," is created successfully")
        else:
            print("Aircraft ", registrationNo, " not available")
    elif action =="3":
        takeofftime = input("Enter takeoffTime? ")
        takepoint = input("Enter takepoint? ")
        aircraft = input("Enter AircraftNo?")
        destination = input("Enter your destination?")
        landingtime = input("Enter landing time?") 
        price = input("Enter price?")
        flightno = input("Enter Flight No? ")
        flightManager.update(flightno,takeofftime,takepoint,aircraft,destination,landingtime,price)
    elif action =="4":
        flightno =input("Enter Flight No? ")
        flightManager.delete(flightno)
    showSubMenu("2")

        

def showManageFlightMenu():
    print("Enter 0 to return to MainMenu")
    print("Enter 1 to List flights")
    print("Enter 2 to Create flight")
    print("Enter 3 to update flight")
    print("Enter 4 to delete flight")




def handleManageAircraftsAction(action):
    if action == "1":
        aircraftManager.list()
    elif action == "2":
        aircraftno =input("Enter Aircraft No? ")
        capacity =input("Enter Aircraft Capacity? ")
        name = input("Enter Aircraft name? ")
        type= input("Enter Aircraft type?")
        aircraftManager.create(capacity,aircraftno,type,name)
        print("Congrats! Your aircraft ",aircraftno," is created successfully")
    elif action == "3":
        capacity = input("Enter Aircraft Capacity? ")
        name = input("Enter Aircraft name? ")
        type = type= input("Enter Aircraft type?")
        aircraftno = input("Enter Aircraft No? ")
        aircraftManager.update(capacity,aircraftno,type,name)
        print(aircraftno,"is updated!")
    elif action == "4":
        aircraftno = input("Enter aircraftno?")
        aircraftManager.delete(aircraftno)
        print(aircraftno,"deleted")
    showSubMenu("1")

def showManageAircraftsMenu():
    print("Enter 0 to return to MainMenu")
    print("Enter 1 to List Aircrafts")
    print("Enter 2 to Create Aircraft")
    print("Enter 3 to update Aircraft")
    print("Enter 4 to delete Aircraft")

def main():    
    flag = True
    while(flag):
        mainMenu()
        option =input()
        if(option== "0"):
            flag=False
        else:
            showSubMenu(option)

main()