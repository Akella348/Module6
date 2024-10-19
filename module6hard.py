import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = list(color)
        self.filled = False
        self.set_sides(*sides)

    def __is_valid_color(self, r, g, b):
        return all(isinstance(v, int) and 0 <= v <= 255 for v in (r, g, b)) # проверка на int и диапазон

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, (int, float)) and side > 0 for side in new_sides)
    # Проверка на размер тип и значение больше 0
    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides) # переопределение на расчет периметра

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:  # если передано одно значение
            new_sides = (new_sides[0],) * self.sides_count  # Создаем кортеж с одинаковыми значениями
        if self.__is_valid_sides(*new_sides): # проверка
            self.__sides = list(new_sides) # добавление

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if self.get_sides():
            self.__radius = self.get_sides()[0] / (2 * math.pi)
        else:
            self.__radius = 1

    def get_square(self):
        return math.pi * math.pow(self.__radius, 2)



class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if not self.get_sides():  # Если стороны не указаны
            self.set_sides(1)  # Устанавливаем стандартные стороны


    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    sides_count = 12  # Указываем 12 рёбер

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if not self.get_sides():  # Если стороны не указаны
            self.set_sides(1)  # Устанавливаем сторону по умолчанию


    def get_volume(self):
        if self.get_sides():  # Проверка на наличие сторон
            return math.pow(self.get_sides()[0], 3)  # Используем одно значение стороны для расчета объёма
        return 0  # Если сторон нет, отдаем 0 или выбрасываем ошибку

# Код для проверки
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)  # Передаем 6 как длину стороны

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())