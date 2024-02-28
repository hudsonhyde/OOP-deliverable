class RetailItem:

    def __init__(self,d,u,p):
        self.__description = d
        self.__units = u
        self.__price = p
    
    def get_description(self):
        return self.__description
    
    def get_units(self):
        return self.__units

    def get_price(self):
        return self.__price



