car_type = eval(input("Nhap loai xe (4 hoac 7 cho): "))
time_wait = eval(input("Nhap thoi gian cho (phut): "))
road = eval(input("Nhap KM da di: "))
open_door_4seats = 11000; road1 = 0.5
open_door_7seats = 12000; road2 = 30
price_4seats1 = 17600; price_time = 750
price_4seats2 = 14500; timefor_free = 5
price_7seats1 = 19600
price_7seats2 = 17100
def taxi4seats():
    amount_road = open_door_4seats
    if road <= road1:
        amount_road = open_door_4seats
    elif road <= road2:
        amount_road = open_door_4seats + (road - road1) * price_4seats1
    else:
        amount_road = open_door_4seats + ((road2 - road1) * price_4seats1) + (road - road2) * price_4seats2
    amount_time = 0
    if time_wait < timefor_free:
        amount_time = 0;
    else:
        amount_time = (time_wait - timefor_free) * price_time
    total_amount = amount_time + amount_road
    return print(f'Tien cuoc| = {amount_time} + {amount_road} = {total_amount}')
def taxi7seats():
    amount_road = open_door_7seats
    if road <= road1:
        amount_road = open_door_7seats
    elif road <= road2:
        amount_road = open_door_7seats + (road - road1) * price_7seats1
    else:
        amount_road = open_door_7seats + ((road2 - road1) * price_7seats1) + (road - road2) * price_7seats2
    amount_time = 0
    if time_wait < timefor_free:
        amount_time = 0;
    else:
        amount_time = (time_wait - timefor_free) * price_time
    total_amount = amount_time + amount_road
    return print(f'Tien cuoc = {amount_time} + {amount_road} = {total_amount}')
if car_type == 4:
    taxi4seats()
else:
    taxi7seats()
