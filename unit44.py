year = int(input("Nhap nam can kiem tra: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'Nam {year} la nam nhuan')
else:
    print(f'Nam {year} la nam khong nhuan')