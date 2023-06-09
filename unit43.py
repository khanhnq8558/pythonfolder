print("Phuong trinh ax + b = 0, hay nhap a va b!!!")
a,b = eval(input("Nhap lan luot theo thu tu a va b: "))
if  a != 0:
    x = -b/a
    print(f'Phuong trinh {a}x + {b} = 0 co nghiem la: x = {x}')
elif a == 0 and b == 0:
    print("Phuong trinh co vo so nghiem")
else:
    print("Phuong trinh vo nghiem")