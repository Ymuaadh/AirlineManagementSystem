from flight import Flight
from aircraftmanager import AircraftManager
class FlightManager():
    Flights = []
    acmgr=AircraftManager()
    def list(self):
        for avalFlight in self.Flights:
            self.show(avalFlight)
    def show(self,avalFlight):
        print(avalFlight.aircraft.registrationNo," ",avalFlight.flightno," ",avalFlight.destination," ",avalFlight.takeofftime," ",avalFlight.landingtime," ",avalFlight.price)
    def create(self,flightno,takeofftime,takepoint,registrationNo,destination,landingtime,price):
        
        aircraft = self.acmgr.find(registrationNo)
        if  aircraft == None:
            print("Aircraft", registrationNo, "is not available")
            return False
        else:
            avalFlight = Flight(flightno,takeofftime,takepoint,aircraft,destination,landingtime,price)
            self.Flights.append(avalFlight)
            return True
    def update(self,flightno,takeofftime,takepoint,aircraft,destination,landingtime,price):
        avalFlight = self.find(flightno)
        avalFlight.takeofftime = takeofftime
        avalFlight.takepoint = takeofftime
        avalFlight.aircraft = aircraft
        avalFlight.destination = destination
        avalFlight.landingtime = landingtime
        avalFlight.price = price
    def delete(self,flightno):
        avalFlight = self.find(flightno)
        self.Flights.append(avalFlight)
    def find(self,flightno):
        for avalFlight in self.Flights:
            if avalFlight.flightno == flightno:
                return avalFlight
            else:
                return None



