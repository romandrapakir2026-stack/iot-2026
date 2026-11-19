class Hotel:
    def __init__(self, name="-", visitors=0, rooms=0, stars=0, city="-"):
        self.__name = name
        self.__visitors = visitors
        self.__rooms = rooms
        self.stars = stars
        self.city = city

    def get_name(self):
        return self.__name

    def get_visitors(self):
        return self.__visitors

    def get_rooms(self): 
        return self.__rooms

    def __str__(self):
        return f"{self.__name}, {self.__visitors}, {self.__rooms}, {self.stars}, {self.city}"

    def __repr__(self):
        return f"Hotel('{self.__name}', {self.__visitors}, {self.__rooms}, {self.stars}, '{self.city}')"

    def __del__(self):
        print("Видалено", self.__name)
    
def main():
    h1 = Hotel("Калина", 16, 4, 2, "Яворів")
    h2 = Hotel("Леополіс", 123132, 45640, 4, "Львів")
    h3 = Hotel("Карпати", 57734, 56787, 3, "Буковель")   
    print(h1)
    print(repr(h1))

    print(h2)
    print(repr(h2))

    print(h3)
    print(repr(h3))
  
main()
