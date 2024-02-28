import CarClass as c

def main():
    
    car1 = c.Car(2008, 'Nissan')

    print('This is for accelerating')
    for i in range(5):
        car1.calc_accelerate()
        print(f'current speed: {car1.get_speed()}')
    
    print('This is for breaking')
    for i in range(5):
        car1.calc_brake()
        print(f'current speed: {car1.get_speed()}')

main()


