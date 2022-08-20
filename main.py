import random

class ToyFabric():
    def __init__(self, name, colors, types):
        self.name = name
        self.colors = colors
        self.types = types

    def purchase_of_raw_materials(self):
        raw_materials = ("вата", "синтепон", "холлофайдер", "синтетичні гранули", "синтепух", "поролон", "сировина")
        print ("ми виготовляємо", self.name, "та купуємо", random.choice(raw_materials))

    def sewing_toys(self):
        print ("ми починаємо шити", self.types)

    def dyeing(self):
        print ("далі ми фарбуємо нашу іграшку в", self.colors)

    def printtoy(self, name, colors, types):
        self.purchase_of_raw_materials()
        self.sewing_toys()
        self.dyeing()




name1 = input("введіть ім'я іграшки: ")
color1 = input("введіть колір, якого буде іграшка: ")
type1 = input("введіть тип іграшки: ")

toy1=ToyFabric(name1, color1, type1)
toy1.printtoy(name1, color1, type1)





