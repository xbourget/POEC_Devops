class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age
    
    def get_species(self):
        return self.species
    
    def get_age(self):
        return self.age
    
    def increase_age(self):
        self.age += 1


class Dog(Animal):
    def __init__(self, breed, age):
        super().__init__('dog', age)
        self.breed = breed
        
    def get_breed(self):
        return self.breed


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__('cat', age)
        self.name = name
        
    def get_name(self):
        return self.name


dog1 = Dog('Golden Retriever', 0)
dog2 = Dog('Kurzhaar', 0.5)
dog3 = Dog('Fox Terrier', 0.2)

cat1 = Cat('Mittens', 1)
cat2 = Cat('Socks', 0.5)
cat3 = Cat('Whiskers', 0.2)

animals = [dog1, dog2, dog3, cat1, cat2, cat3]

for animal in animals:
    print(animal.get_species(), end=' ')
    if isinstance(animal, Dog):
        print(animal.get_breed(), end=' ')
    elif isinstance(animal, Cat):
        print(animal.get_name(), end=' ')
    print(animal.get_age())

for animal in animals:
    animal.increase_age()

for animal in animals:
    print(animal.get_species(), end=' ')
    if isinstance(animal, Dog):
        print(animal.get_breed(), end=' ')
    elif isinstance(animal, Cat):
        print(animal.get_name(), end=' ')
    print(animal.get_age())
