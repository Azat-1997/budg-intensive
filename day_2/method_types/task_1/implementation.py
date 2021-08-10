class Coffee:
    def __init__(self, ingridients):
        self.ingridients = ingridients

    @classmethod
    def create_latte(cls):
       return Coffee({"espresso", "milk", "syrup"})

    @classmethod
    def create_capuccino(cls):
       return Coffee({"espresso", "milk"})

    @classmethod
    def create_glace(cls):
       return Coffe({"coffee", "icecream", "chocolate"})
