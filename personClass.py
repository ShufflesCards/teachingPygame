class Person():
    def __init__(self, name, age, hight, grade, hair):
        self.name = name
        self.age = age
        self.hight = hight
        self.grade = grade
        self.hair = hair
    def __str__(self):
        return f"{self.name} is {self.age} years old, in grade {self.grade} with {self.hair} colored hair. {self.name} is also {self.hight} in tall."
        

ben = Person("Ben",18, 65, 12, "brown")
nicoll = Person("Nicoll", 18, 40, 12, "brown")
print(ben)
print(nicoll)