
from passanger import Passanger
class PassagerManager:
    passangersInfo = []
    file = open("passangers.txt","a+")
    def __init__(self):
        self.file.seek(0)
        for Passanger_line in self.file:
            self.passangersInfo.append(Passanger.parse(Passanger_line))


    def list(self):
        for info in self.passangersInfo:
            self.show(info)


    def show(self,info):
        print(info.name," ",info.age," ",info.PhoneNo," ",info.Email," ",info.Address)


    def create(self,name,age,PhoneNo,Email,Address):
        info=Passanger(name,age,PhoneNo,Email,Address)
        self.passangersInfo.append(info)
        self.file.write(f"{str(info)}\n")
        self.file.flush()


    def find(self,PhoneNo):
        for info in self.passangersInfo:
            if info.PhoneNo == PhoneNo:
                return info
        return None

    def delete(self,PhoneNo):
        info = self.find(PhoneNo)
        self.passangersInfo.remove(info)
        self.__refreahFile()

    def update(self,name,age,PhoneNo,Email,Address):
        info = self.find(PhoneNo)
        info.name = name
        info.age=age
        info.Email=Email        
        info.Address = Address
        info.PhoneNo = PhoneNo
        self.__refreahFile()

    def __refreahFile(self):
        self.file=open("passangers.txt","w")
        for info in self.passangersInfo:
            self.file.write(f"{str(info)}\n")
            self.file.write("\n")
        
    


