class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def get_info(self):
        return f"Имя: {self.name}, ID: {self.id}"

class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self,name, id)
        self.department = department
    
    def manage_project(self):
        return f"{self.name} он(а) руководит в отделе {self.department}."

class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self,name, id)
        self.specialization = specialization
    
    def perform_maintenance(self):
        return f"{self.name} он(а) специализируется в области {self.specialization}."

class TechManager(Technician,Manager):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self,name,id,department)
        Technician.__init__(self,name,id,specialization)
        #self.department=department
        #self.specialization=specialization
        self.team = []
    
    def add_employee(self, employee):
        self.team.append(employee)
    
    def get_team_info(self):
        if not self.team:
            return "Команды нет."
        return "\n".join([employee.get_info() for employee in self.team])

employee1 = Employee("Даня", 11)
print(employee1.get_info())

manager = Manager("Лёшка", 12, "Продажи")
print(manager.get_info())
print(manager.manage_project())

technician = Technician("Вадик", 13, "электротехника")
print(technician.get_info())
print(technician.perform_maintenance())

tech_manager = TechManager("", 14, "IT", "сеть")
print(tech_manager.get_info())
print(tech_manager.manage_project())
print(tech_manager.perform_maintenance())

tech_manager.add_employee(employee1)
tech_manager.add_employee(manager)
tech_manager.add_employee(technician)

print("Team Info:")
print(tech_manager.get_team_info())