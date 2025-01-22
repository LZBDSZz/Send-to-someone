import os
import time
Member = [
    '0888888888',
    '01234',
    '19132',
    '0629158938'
]

Mydata = {}
Pricin = None
CalculatedPrice = None
deductedPrice = None

def console_clear():
    if os.system("clear") != 0:
        if os.system("cls") != 0:
            for _ in range(25):
                print("\n\n")

def place_x():
    print('loading data')
    global Pricin, CalculatedPrice, deductedPrice
    time.sleep(2)
    console_clear()
    Price = {
        'AtStore': {
            '1': 150,
            '2': 299,
            '3': 445,
            '4': 599,
            '5': 745,
            '6': 899,
            '7': 1040,
            '8': 1120,
            '10': 1399
        },
        'ofProvince': {
            '1': 180,
            '2': 329,
            '3': 475,
            '4': 629,
            '5': 775,
            '6': 929,
            '7': 1070,
            '8': 1150,
            '10': 1429
        },
        'otherProvinces': {
            '1': 250,
            '2': 399,
            '3': 545,
            '4': 699,
            '5': 845,
            '6': 999,
            '7': 1140,
            '8': 1220,
            '10': 1499
        }
    }

    Mydata['Identifier'] = {}

    Mydata['Identifier']['Name'] = input('your Name: ')
    Mydata['Identifier']['Address'] = input('your Address: ')
    Mydata['Identifier']['Number'] = input('your Number: ')

    while not Mydata['Identifier']['Number'].isdigit():
        Mydata['Identifier']['Number'] = input('your (Number): ')

    Mydata['IsMember'] = False
    for id in Member:
        if id == Mydata['Identifier']['Number']:
            Mydata['IsMember'] = True
            break

    while True:
        Mydata['logisType'] = input('\n\n [-choose logistics type-]\n(1) In the Province [+30฿]\n(2) Out of the Province [+100฿]\n(3) Pick up (In-store pickup)\nSelect : ')
        if Mydata['logisType'] in ['1', '2', '3']:
            break
        else:
            print('Error Please select valid data')
            time.sleep(0.5)
            console_clear()

    if Mydata['logisType'] == '1':
        while True:
            Mydata['weight'] = input('\n\n1 kg : 180฿\n2 kg : 329฿\n3 kg : 475฿\n4 Kg : 629฿\n5 Kg : 775฿\n6 Kg : 929฿\n7 Kg : 1070฿\n8 Kg : 1150฿\n10 Kg : 1429฿\nyour weight (kg.) (+30฿ logistic charged): ')
            if Mydata['weight'].isdigit():
                if Mydata['weight'] in Price['ofProvince']:
                    Pricin = Price['ofProvince'][Mydata['weight']]
                    break
                else:
                    print('choose the correct value!')
                    time.sleep(0.5)
                    console_clear()

    elif Mydata['logisType'] == '2':
        while True:
            Mydata['weight'] = input('\n\n1 kg : 250฿\n2 kg : 399฿\n3 kg : 545฿\n4 Kg : 699฿\n5 Kg : 845฿\n6 Kg : 999฿\n7 Kg : 1140฿\n8 Kg : 1220฿\n10 Kg : 1499฿\nyour weight (kg.) (+100฿ logistic charged): ')
            if Mydata['weight'].isdigit():
                if Mydata['weight'] in Price['otherProvinces']:
                    Pricin = Price['otherProvinces'][Mydata['weight']]
                    break
                else:
                    print('choose the correct value!')
                    time.sleep(0.5)
                    console_clear()
    elif Mydata['logisType'] == '3':
        while True:
            Mydata['weight'] = input('\n\n1 kg : 150฿\n2 kg : 299฿\n3 kg : 445฿\n4 Kg : 599฿\n5 Kg : 745฿\n6 Kg : 899฿\n7 Kg : 1040฿\n8 Kg : 1120฿\n10 Kg : 1399฿\nyour weight (kg.) (no logistic charged): ')
            if Mydata['weight'].isdigit():
                if Mydata['weight'] in Price['AtStore']:
                    Pricin = Price['AtStore'][Mydata['weight']]
                    break
                else:
                    print('choose the correct value!')
                    time.sleep(0.5)
                    console_clear()

    def calcu_price():
        if Mydata['IsMember']:
            arg1 = Pricin
            arg2 = Pricin * (100 - 15) / 100
            return arg2, arg1 - arg2
        return Pricin, 0

    CalculatedPrice, deductedPrice = calcu_price()

    print(f'\n\nName: {Mydata["Identifier"]["Name"]}\nAddress: {Mydata["Identifier"]["Address"]}\nNumber: {Mydata["Identifier"]["Number"]}\nHas MemberShip: {"yes" if Mydata["IsMember"] else "not"}\nPrice: {CalculatedPrice}\n{f"Discount: {deductedPrice}฿" if Mydata["IsMember"] else ""}')
    while True:
        Mydata['Money'] = input(f'\nPrice total ({CalculatedPrice})\nPay your money: ')
        if Mydata['Money'].isdigit():
            if int(Mydata['Money']) >= CalculatedPrice:
                global Change
                Change = int(Mydata['Money']) - CalculatedPrice
                time.sleep(2)
                print(f'\nCash change: {Change}')
                break
            else:
                print('no enough money')
                time.sleep(2)
                print('[Info] Returning to information page...')
                time.sleep(2)
                console_clear()
                return False

    return True

def confirm_page():
    while True:
        Confirm = input('Are you sure to confirm? (y/n/cancel): ')
        if Confirm.lower() in ['yes', 'y']:
            console_clear()
            print('[Info] Order summarizing..')
            time.sleep(2)
            print('done.')
            time.sleep(2)
            print('loading data..')
            time.sleep(1)
            print('all data has been loaded..')
            time.sleep(1)
            console_clear()
            print(' [User information]')
            print(f'Name: {Mydata["Identifier"]["Name"]}')
            print(f'Address: {Mydata["Identifier"]["Address"]}')
            print(f'Number: {Mydata["Identifier"]["Number"]}')
            print(f'Has MemberShip: {"yes" if Mydata["IsMember"] else "not"}')
            print(f'Price: {CalculatedPrice}\n{f"Discount: {deductedPrice}฿" if Mydata["IsMember"] else ""}')
            print('---------------------------------')
            print('---------- Order Info -----------')
            print(f'Raw price: {Pricin}฿')
            print(f'Calculated price: {CalculatedPrice}{f"\nDeducted Price: {deductedPrice}฿" if Mydata["IsMember"] else ""}')
            print(f'Cash Recived: {Mydata['Money']}')
            print(f'Cash change: {Change}')
            return 'done'
        elif Confirm.lower() in ['no', 'n']:
            console_clear()
            print('[Info] Returning to information page...')
            time.sleep(2)
            place_x()
            return 'editInfo'
        elif Confirm.lower() == 'cancel':
            console_clear()
            time.sleep(1)
            print('[Info] Your order has been canceled!')
            return 'cancel'
        else:
            print('Invalid input. Please type y/n/cancel.')

while not place_x():
    pass

print(f'\n\nName: {Mydata["Identifier"]["Name"]}\nAddress: {Mydata["Identifier"]["Address"]}\nNumber: {Mydata["Identifier"]["Number"]}\nHas MemberShip: {"yes" if Mydata["IsMember"] else "not"}\nPrice: {CalculatedPrice}\n{f"Discount: {deductedPrice}฿" if Mydata["IsMember"] else ""}')

while True:
    action = confirm_page()
    if action == 'cancel':
        print('[Info] Your order has been canceled!')
        break
    elif action == 'editInfo':
        print('\n[Info] User information updated.')
    elif action == 'done':
        break
