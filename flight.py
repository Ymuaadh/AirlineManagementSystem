class Flight:
    def __init__(self,flightno,takeofftime,takepoint,destination,landingtime,price):
        self.flightno = flightno
        self.takeofftime = takeofftime
        self.takepoint = takepoint
        self.destination = destination
        self.landingtime = landingtime
        self.price = price

    def __str__(self):
        return f"{self.flightno}\t{self.takeofftime}\t{self.takepoint}\t{self.destination}\t{self.landingtime}\t{self.price}"

    def parse(line: str):
        flightno,takeofftime,takepoint,destination,landingtime,price = line.split("\t")
        return Flight(flightno,takeofftime,takepoint,destination,landingtime,price)
        