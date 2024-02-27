import CellPhoneClass as cp

def main():
    
    phone = cp.CellPhone('apple', 'Iphone 15', 1099) #This is the instance
    
    
    price = input('What is your phone price: ')
    phone.set_retail_price(price)


    print(f'Phone Manufacturer: {phone.get_manufact()}')
    print(f'Phone Model: {phone.get_model()}')
    print(f'Phone price: ${phone.get_retail_price()}')

main()
