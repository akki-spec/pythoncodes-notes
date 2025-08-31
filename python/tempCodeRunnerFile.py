class car:
    def set_details(self, brand, color):
        self.brand = brand
        self.color = color

    def show_details(self):
        print(f'this car is a {self.color}{self.brand}')

car1 = car()
car1.set_details('tesla','red')

car2 = car()
car2.set_details('bmw','white')

car1.show_details()
car2.show_details()