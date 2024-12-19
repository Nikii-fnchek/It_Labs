class Circle:
    def __init__(self, radius):
        self.radius = radius  # Это радиус

    def get_radius(self):
        return self.radius  # Это штука (метод) возвращает значение радиуса

    def set_radius(self, new_radius):
        self.radius = new_radius  # Это изменяет радиус круга
# Далее
# Создаем объект
my_circle = Circle(5)

# Выводим текущий радиус
print(f"Текущий радиус круга: {my_circle.get_radius()}")

# Изменяем радиус кружочка
my_circle.set_radius(10)

# Выводим новый радиус
print(f"Новый радиус круга: {my_circle.get_radius()}")