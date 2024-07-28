class Product:
    def getPrice(self):
        return self.__price

    def setPrice(self, val):
        if val < 0:
            self.__price = 0 
            return 

        self.__price = val 

obj = Product()
obj.setPrice(-15)
print(obj.getPrice())