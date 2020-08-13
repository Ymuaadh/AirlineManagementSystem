class Booking:
    def __init__(self,destination,TimeOfFlight,TypeOfFlight,Price,SitNumber,name):
        self.name = name
        self.SitNumber = SitNumber
        self.Price = Price
        self.TypeOfFlight = TypeOfFlight
        self.TimeOfFlight = TimeOfFlight
        self.destination = destination


    def __str__(self):
        return f"{self.name}\t{self.SitNumber}\t{self.Price}\t{self.TypeOfFlight}\t{self.TimeOfFlight}\t{self.destination}"

    def parse(line: str):
        name,SitNumber,Price,TypeOfFlight,TimeOfFlight,destination = line.split("\t")
        return Booking(name,SitNumber,Price,TypeOfFlight,TimeOfFlight,destination)
