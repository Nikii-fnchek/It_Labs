class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}"
car1=Vehicle('Tesla','Model X')
class Car(Vehicle):
    def __init__(self,make,model,fuel_type):
        super().__init__(make,model)
        self.fuel_type=fuel_type
    def get_info(self):
        return f"{super().get_info()}, Топливо: {self.fuel_type}"
car2=Car('Tesla','Medol Y','electricity')
print(car1.get_info())
print(car2.get_info())