
from passanger import Passanger
class PassagerManager:
    passangersInfo = []
    def list(self):
        for info in self.passangersInfo:
            self.show(info)
    def show(self,info):
        print(info.name," ",info.age," ",info.PhoneNo," ",info.Email," ",info.Address)
    def create(self,name,age,Email,PhoneNo,Address):
        info=Passanger(name,age,Email,PhoneNo,Address)
        self.passangersInfo.append(info)
    def find(self,PhoneNo):
        for info in self.passangersInfo:
            if info.PhoneNo == PhoneNo:
                return info
            else:
                return None
    def delete(self,PhoneNo):
        info = self.find(PhoneNo)
        self.passangersInfo.remove(info)
    def update(self,name,age,PhoneNo,Email,Address):
        info = self.find(PhoneNo)
        info.name = name
        info.age=age
        info.Email=Email        
        info.Address = Address
        info.PhoneNo = PhoneNo
    
        
    


manager= PassagerManager()
manager.create("ola","12","olaniteolalekan@gmail.com","07038386817","Ogun")
manager.update("ola","12","olaniteolalekan@gmail.com","07052003532","Ogun")
manager.list()