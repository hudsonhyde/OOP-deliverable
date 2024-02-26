class CellPhone:

    def __init__(self, manufacturer, model, price):
        self.__manufact = manufacturer
        self.__model = model
        self.__retail_price = price


    def set_manufact(self, manufacturer):
        self.__manufact = manufacturer
    
    def set_model(self, model):
        self.__model = model

    def set_retail_price(self, price):
        self.__retail_price = price 
        if price == 1099:
            price -= 100
            
    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price