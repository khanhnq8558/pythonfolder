def tinh_tien_dien(so_dien):
    # Các mức giá điện theo 6 bậc thông thường
    muc_gia_dien = [
        {'muc': 50, 'gia': 1678},
        {'muc': 100, 'gia': 1734},
        {'muc': 200, 'gia': 2014},
        {'muc': 300, 'gia': 2536},
        {'muc': 400, 'gia': 2834},
        {'muc': -1, 'gia': 2927}
    ]
    
    tong_tien = 0
    
    # Tính tiền điện theo từng bậc giá và cộng dồn
    if so_dien <= muc_gia_dien[0]['muc']:
        tong_tien = so_dien * muc_gia_dien[0]['gia']
    elif so_dien <= muc_gia_dien[1]['muc']:
        tong_tien = (so_dien - muc_gia_dien[0]['muc']) * muc_gia_dien[1]['gia']
        tong_tien += muc_gia_dien[0]['muc'] * muc_gia_dien[0]['gia']
    elif so_dien <= muc_gia_dien[2]['muc']:
        tong_tien = (so_dien - (muc_gia_dien[1]['muc'])) * muc_gia_dien[2]['gia']
        tong_tien += (muc_gia_dien[1]['muc'] - muc_gia_dien[0]['muc']) * muc_gia_dien[1]['gia']
        tong_tien += muc_gia_dien[0]['muc'] * muc_gia_dien[0]['gia']
    elif so_dien <= muc_gia_dien[3]['muc']:
        tong_tien = (so_dien - muc_gia_dien[2]['muc']) * muc_gia_dien[3]['gia']
        tong_tien += (muc_gia_dien[2]['muc'] -(muc_gia_dien[1]['muc'])) * muc_gia_dien[2]['gia']
        tong_tien += (muc_gia_dien[1]['muc'] - muc_gia_dien[0]['muc']) * muc_gia_dien[1]['gia']
        tong_tien += muc_gia_dien[0]['muc'] * muc_gia_dien[0]['gia']
    elif so_dien <= muc_gia_dien[4]['muc']:
        tong_tien = (so_dien - muc_gia_dien[3]['muc']) * muc_gia_dien[4]['gia']
        tong_tien += (muc_gia_dien[3]['muc'] - muc_gia_dien[2]['muc']) * muc_gia_dien[3]['gia']
        tong_tien += (muc_gia_dien[2]['muc'] -(muc_gia_dien[1]['muc'])) * muc_gia_dien[2]['gia']
        tong_tien += (muc_gia_dien[1]['muc'] - muc_gia_dien[0]['muc']) * muc_gia_dien[1]['gia']
        tong_tien += muc_gia_dien[0]['muc'] * muc_gia_dien[0]['gia']
    else:
        tong_tien = (so_dien - muc_gia_dien[4]['muc']) * muc_gia_dien[5]['gia']
        tong_tien += (muc_gia_dien[4]['muc'] - muc_gia_dien[3]['muc']) * muc_gia_dien[4]['gia']
        tong_tien += (muc_gia_dien[3]['muc'] - muc_gia_dien[2]['muc']) * muc_gia_dien[3]['gia']
        tong_tien += (muc_gia_dien[2]['muc'] -(muc_gia_dien[1]['muc'])) * muc_gia_dien[2]['gia']
        tong_tien += (muc_gia_dien[1]['muc'] - muc_gia_dien[0]['muc']) * muc_gia_dien[1]['gia']
        tong_tien += muc_gia_dien[0]['muc'] * muc_gia_dien[0]['gia']
    
    return tong_tien

# Nhập vào số điện tiêu thụ
so_dien_tieu_thu = eval(input("Nhập vào số điện tiêu thụ (kWh): "))

# Tính toán và in ra tổng tiền phải trả
tong_tien_dien = tinh_tien_dien(so_dien_tieu_thu)
print("Tổng tiền điện phải trả: ", tong_tien_dien, " VND")
