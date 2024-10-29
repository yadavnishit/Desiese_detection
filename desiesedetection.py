body_temp = float(input('Enter body temp in Fe :'))
if body_temp == 98.7:
    print('Malaria not found')
    pt_count = float(input('Enter platelet count in decimcal  :'))
    if pt_count < 1.8:
        print('Dengue')
    else:
        print('You are lucky you are fit')
elif body_temp >98.7 and body_temp <= 99:
    print('Normal Temp')

elif body_temp > 99 and body_temp <102:

    pt_count = float(input('Enter platelet count in decimcal'))
    if pt_count < 1.8:
        print('Dengue and Malaria')
    else:
        print(' My be Maraira')
elif body_temp > 102:
    pt_count = float(input('Enter platelet count in decimcal'))
    if pt_count < 1.8:
        print('Severe Condition get admit in hospital')
    else:
        print('High Fever with Malaria')
else:
    print('Normal Person')