class Booking:
    def __init__(self,destination,TimeOfFlight,TypeOfFlight,Price,SitNumber,name):
        self.name = name
        self.SitNumber = SitNumber
        self.Price = Price
        self.TypeOfFlight = TypeOfFlight
        self.TimeOfFlight = TimeOfFlight
        self.destination = destination

