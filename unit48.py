def cal_tax(salary,persons):
    tax_list = [
        {'level1': 60000000, 'tax': 0.05},
        {'level2': 120000000, 'tax': 0.1},
        {'level3': 216000000, 'tax': 0.15},
        {'level4': 384000000, 'tax': 0.2},
        {'level5': 624000000, 'tax': 0.25},
        {'level6': 960000000, 'tax': 0.3},
        {'level7': 960000000, 'tax': 0.35}
    ]
    list_tax_speacial = [
        {'owner_income': 11000000},
        {'depend_person': 4400000}
    ]
    allowances = (((salary / 12) - list_tax_speacial[0]['owner_income']) - (persons * list_tax_speacial[1]['depend_person'])) * 12
    amount = 0
    if  allowances <= tax_list[0]['level1']:
        amount = tax_list[0]['level1'] * tax_list[0]['tax']
    elif allowances <= tax_list[1]['level2']:
        amount = (allowances - tax_list[0]['level1']) * tax_list[1]['tax']
        amount += tax_list[0]['level1'] * tax_list[0]['tax']
    elif allowances <= tax_list[2]['level3']:
        amount = (allowances - tax_list[1]['level2']) * tax_list[2]['tax']
        amount += (allowances - tax_list[0]['level1']) * tax_list[1]['tax']
        amount += tax_list[0]['level1'] * tax_list[0]['tax']
    elif allowances <= tax_list[3]['level4']:
        amount = (allowances - tax_list[2]['level3']) * tax_list[3]['tax']
        amount += (allowances - tax_list[1]['level2']) * tax_list[2]['tax']
        amount += (allowances - tax_list[0]['level1']) * tax_list[1]['tax']
        amount += tax_list[0]['level1'] * tax_list[0]['tax']
    elif allowances <= tax_list[4]['level5']:
        amount = (allowances - tax_list[3]['level4']) * tax_list[4]['tax']
        amount += (allowances - tax_list[2]['level3']) * tax_list[3]['tax']
        amount += (allowances - tax_list[1]['level2']) * tax_list[2]['tax']
        amount += (allowances - tax_list[0]['level1']) * tax_list[1]['tax']
        amount += tax_list[0]['level1'] * tax_list[0]['tax']
    elif allowances <= tax_list[5]['level6']:
        amount = (allowances - tax_list[4]['level5']) * tax_list[5]['tax']
        amount += (allowances - tax_list[3]['level4']) * tax_list[4]['tax']
        amount += (allowances - tax_list[2]['level3']) * tax_list[3]['tax']
        amount += (allowances - tax_list[1]['level2']) * tax_list[2]['tax']
        amount += (allowances - tax_list[0]['level1']) * tax_list[1]['tax']
        amount += tax_list[0]['level1'] * tax_list[0]['tax']
    elif allowances <= tax_list[6]['level7']:
        amount = (allowances - tax_list[5]['level6']) * tax_list[6]['tax']
        amount += (allowances - tax_list[4]['level5']) * tax_list[5]['tax']
        amount += (allowances - tax_list[3]['level4']) * tax_list[4]['tax']
        amount += (allowances - tax_list[2]['level3']) * tax_list[3]['tax']
        amount += (allowances - tax_list[1]['level2']) * tax_list[2]['tax']
        amount += (allowances - tax_list[0]['level1']) * tax_list[1]['tax']
        amount += tax_list[0]['level1'] * tax_list[0]['tax']
    return amount
income = eval(input("Nhap thu nhap nam cua ban (Trieu) : "))
persons = eval(input("Nhap so nguoi phu thuoc: "))
total_amount_tax = cal_tax(income,persons)
print(f'Tong tien giam tru la: {total_amount_tax:.1f} VND')