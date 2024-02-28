import RetailItemClass as ri 

def main():

    item1 = ri.RetailItem('Jacket', 12, 59.95)
    item2 = ri.RetailItem('Designer Jeans', 40, 34.95)
    item3 = ri.RetailItem('Shirt', 20, 24.95)

   
    
    print(f'Item 1 are {item1.get_description()} and contains {item1.get_units()} in inventory and cost ${item1.get_price():.2f} per item')
    print(f'Item 2 are {item2.get_description()} and contains {item2.get_units()} in inventory and cost ${item2.get_price():.2f} per item')
    print(f'Item 3 are {item3.get_description()} and contains {item3.get_units()} in inventory and cost ${item3.get_price():.2f} per item')

main()
    