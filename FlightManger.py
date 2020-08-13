from flight import Flight
class FlightManager():
    Flights = []
    file = open("flights.txt","a+")
    def __init__(self,acmgr):
        self.acmgr=acmgr
        self.file.seek(0)
        for Flight_line in self.file:
            self.Flights.append(Flight.parse(Flight_line))

    def list(self):
        for avalFlight in self.Flights:
            self.show(avalFlight)
    def show(self,avalFlight):
        print(avalFlight.flightno," ",avalFlight.destination," ",avalFlight.takeofftime," ",avalFlight.landingtime," ",avalFlight.price)


    def create(self,flightno,takeofftime,takepoint,registrationNo,destination,landingtime,price):
        aircraft = self.acmgr.find(registrationNo)
        if  aircraft == None:
            print("Aircraft", registrationNo, "is not available")
            return False
        else:
            avalFlight = Flight(flightno,takeofftime,takepoint,destination,landingtime,price)
            self.Flights.append(avalFlight)
            self.file.write(f"{str(avalFlight)}\n")
            self.file.flush()
            return True

    def __refreshFile(self):
        self.file = open("flights.txt","w")
        for avalFlight in self.Flights:
            self.file.write(f"{str(avalFlight)}\n")
            self.file.write("\n")



    def update(self,flightno,takeofftime,takepoint,aircraft,destination,landingtime,price):
        avalFlight = self.find(flightno)
        avalFlight.takeofftime = takeofftime
        avalFlight.takepoint = takeofftime
        avalFlight.aircraft = aircraft
        avalFlight.destination = destination
        avalFlight.landingtime = landingtime
        avalFlight.price = price
        self.__refreshFile()


    def delete(self,flightno):
        avalFlight = self.find(flightno)
        self.Flights.append(avalFlight)
        self.__refreshFile()


    def find(self,flightno):
        for avalFlight in self.Flights:
            if avalFlight.flightno == flightno:
                return avalFlight
            else:
                return None



