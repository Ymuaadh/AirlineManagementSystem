class Aircraft:
    def __init__(self,capacity,registrationNo,types,name):
        self.capacity=capacity
        self.registrationNo=registrationNo
        self.types=types
        self.name=name
        
        

    def __str__(self):
        return f"{self.capacity}\t{self.registrationNo}\t{self.types}\t{self.name}"

    def parse(line: str):
        capacity, registrationNo, types, name = line.split("\t")
        capacity = int(capacity)
        return Aircraft(capacity, registrationNo, types, name)
        