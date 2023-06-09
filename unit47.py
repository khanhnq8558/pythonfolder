def choose_room_type(type,nites):
    room_type_list = [
        {'standard': 1, 'price': 1260000},
        {'superior_garden_view': 2, 'price': 1550000},
        {'superior_ocean_view': 3, 'price': 1830000},
        {'garden_view_bungalow': 4, 'price': 1830000},
        {'pool_view_bungalow': 5, 'price': 2120000},
        {'family_room': 6, 'price': 2120000},
        {'beach_front_bungalow': 7, 'price': 2540000},
        {'vip_sea_view': 8, 'price': 4800000}
    ]
    dis_count_list = [
        {'level_1': 2, 'discount': 0.25},
        {'level_2': 3, 'discount': 0.25},
        {'level_3': 4, 'discount': 0.3}
    ]
    amount = 0
    if type == room_type_list[0]['standard']:
        amount = room_type_list[0]['price']*nites
    elif type == room_type_list[1]['superior_garden_view']:
        amount = room_type_list[1]['price']*nites
    elif type == room_type_list[2]['superior_ocean_view']:
        amount = room_type_list[2]['price']*nites
    elif type == room_type_list[3]['garden_view_bungalow']:
        amount = room_type_list[3]['price']*nites
    elif type == room_type_list[4]['pool_view_bungalow']:
        amount = room_type_list[4]['price']*nites
    elif type == room_type_list[5]['family_room']:
        amount = room_type_list[5]['price']*nites
    elif type == room_type_list[6]['beach_front_bungalow']:
        amount = room_type_list[6]['price']*nites
    else: #type == room_type_list[7]['vip_sea_view']:
        amount = room_type_list[7]['price']*nites
    if nites >= dis_count_list[0]['level_1'] and nites <= dis_count_list[1]['level_2']:
        amount = amount - (amount * 0.25)
    elif nites >= dis_count_list[2]['level_3']:
        amount = amount - (amount * 0.3)
    return amount

print("""
           1. Standard
           2. Superior Garden View
           3. Superior Ocean View
           4. Garden View Bungalow
           5. Pool View Bungalow
           6. Family Room
           7. Beach Front Bungalow
           8. VIP sea view
        """)
room_type = int(input("Nhap loai Phong: "))
room_nights = int(input("Nhap so dem o: "))
total_amount = choose_room_type(room_type,room_nights)
print(f'Tong tien phai thanh toan la: {total_amount} VND')