#!/usr/bin/env python3

def action():
    print("Please choose if you want to:\n Send a Thank You or \nCreate a Report")
    response = str(input("==> ")).strip()
    if response.lower() == 'send a thank you':
        send_a_thankyou_note()
    elif response.lower() == 'create a report':
        create_a_report()
    else:
        print('Invalid Response')
        action()
        

def send_a_thankyou_note():
    donors = ['Mufasa', 100, 'Sarabi', 200, 'Simba', 500, 'Nala', 400, 'Kiara', 300, 'Kovu', 600, 'Timon', 700, 'Pumbaa', 800, 'Simba', 200, 'Timon', 100, 'Sarabi', 400, 'Mafasa', 600, 'Simba', 700, 'Timon', 800, 'Kiara', 200]
    names = donors[0:len(donors):2]
    print("Please enter the donor's full name")
    response = input("==> ").strip()
    if response == 'list':
        for i in range(len(names)):
            print names[i]
        response = input("==> ").strip()
        donors.append(response)
    else:
        donors.append(response)
    print('Please enter the donation amount')
    response = input("==> ")
    try:
        val = int(response)
    except:
        print('Error: Amount entered is not a number')    
        while True:
            print('Please enter the donation amount')
            response = input("==> ")

def donation():
    print('Please enter the donation amount')
    response = input("==> ")
    try:
        val = int(response)
    except ValueError:
        print('Error: Amount entered is not a number')
        donation()
    new_donors = send_a_thankyou_note()
    donors.append(response)

def create_a_report():
    """Create a report based on the response chosen by the user"""
    print('Create a report')


if __name__ == "__main__":
    action()
    #donation()
