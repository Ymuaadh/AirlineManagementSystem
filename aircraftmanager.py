
from Aircraft import Aircraft
class AircraftManager:
    aircrafts = []
    def list(self):
        for a in self.aircrafts:
            self.show(a)
    def show(self,a):
       print(a.capacity," ",a.registrationNo)
    def create(self,capacity,registrationNo,types,name):
        a=Aircraft(capacity,registrationNo,types,name)
        self.aircrafts.append(a)
    def update(self,capacity,registrationNo,types,name):
        a = self.find(registrationNo)
        a.capacity=capacity
        a.types=types
        a.name=name
    def delete(self,registrationNo):
        a =self.find(registrationNo)
        self.aircrafts.remove(a)
      
    def find(self,registrationNo):
        for a in self.aircrafts:
            if a.registrationNo==registrationNo:
                return a
        return None
   



