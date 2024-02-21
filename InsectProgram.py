import InsectClass as i 


def main():
    mosquito = i.Insect()
    housefly = i.Insect()

    mosquito.calc_flight()
    housefly.calc_flight()

    print(f'The mosquito can travel up to {mosquito.get_flight()} miles')
    print(f'The horsefly can travel up to {housefly.get_flight()} miles')

main()


    

