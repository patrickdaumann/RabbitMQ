class Person:

    def __init__(self, name: str, age: int, city: str) -> None:
        self.name = name
        self.age = age
        self.city = city

    def __str__(self) -> str:
        return f"{self.name}, {self.age} years old, from {self.city}"

