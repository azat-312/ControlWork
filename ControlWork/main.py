class Person():

    def __init__(self, name, age, City):
        self.name = name
        self.age = age
        self.city = City
    def introduce (self):
        return print(f'Привет, меня зовут {self.name}, мне {self.age} лет, я живу в {self.city}')
    def __str__(self):
        return f'имя {self.name}, возраст {self.age}, город {self.city}'
    def is_adult(self):
        if self.age > 18:
            print(True)
        else:
            print(False)
Persons1 = Person("Максим", 19,"Голандия")
print(Persons1.introduce())
print(str(Persons1))
print(Persons1.is_adult())