


class Vehicle:
    def __init__(self, name):
        self.name = name
        
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print(f"Driving {self.name} car")

class Bike(Vehicle):
    def drive(self):
        print(f"Driving {self.name} bike")

class VehicleFactory:
    def create_vehicle(self, vehicle_type, name):
        if vehicle_type == 'car':
            return Car(name)
        elif vehicle_type == 'bike':
            return Bike(name)

vehicle_factory = VehicleFactory()
vehicle1 = vehicle_factory.create_vehicle('car', 'Mercedes')
vehicle2 = vehicle_factory.create_vehicle('bike', 'Ducati')

vehicle1.drive()
vehicle2.drive()
