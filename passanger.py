class Passanger:
    def __init__(self,name,age,PhoneNo,Email,Address):
        self.name = name
        self.age = age
        self.PhoneNo =PhoneNo
        self.Email = Email
        self.Address = Address 
    
    def __str__(self):
        return f"{self.name}\t{self.age}\t{self.PhoneNo}\t{self.Email}\t{self.Address}"

    def parse(line: str):
        name,age,PhoneNo,Email,Address = line.split("\t")
        return Passanger(name,age,PhoneNo,Email,Address)