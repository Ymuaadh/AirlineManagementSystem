
from Aircraft import Aircraft
class AircraftManager:
    aircrafts = []
    file = open("Aircrafts.txt", "a+")
    def __init__(self):
        self.file.seek(0)
        for Aircraft_line in self.file:
            self.aircrafts.append(Aircraft.parse(Aircraft_line))

    
    def list(self):
        for a in self.aircrafts:
            self.show(a)

    def show(self,a):
       print(a.capacity," ",a.registrationNo," ",a.types," ",a.name)

    def create(self,capacity,registrationNo,types,name):
        a=Aircraft(capacity,registrationNo,types,name)
        self.aircrafts.append(a)
        self.file.write(f"{str(a)}\n")
        self.file.flush()
        

    def update(self,capacity,registrationNo,types,name):
        a = self.find(registrationNo)
        a.capacity=capacity
        a.types=types
        a.name=name
        self.__refreshFile()

    def delete(self,registrationNo):
        a =self.find(registrationNo)
        self.aircrafts.remove(a)
        self.__refreshFile()
    def __refreshFile(self):
        self.file= open("Aircrafts.txt","w")
        for a in self.aircrafts:
            self.file.write(str(a))
            self.file.write("\n")
      
    def find(self,registrationNo):
        for a in self.aircrafts:
            if a.registrationNo==registrationNo:
                return a
        return None
   

