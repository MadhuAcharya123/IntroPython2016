#!/usr/bin/env python3

fruits = ['Apples','Pears','Oranges','Peaches']

def showfruits(fruits):
    for i in fruits:
        print (i)        

def addfruit():
    print('Enter another fruit to add to the list:')
    response = input("==> ").strip()
    fruits.append(response) #add the user inputted fruit at the end of the list# 
    return fruits


def enternum():
    """Enter a number from screen and print the fruit in that position starting at 1."""
    print(('Enter a number from 1 to ') + str(len(fruits)) + (':'))
    response = str(input("==> ")).strip()
    if (int(response) == 0 or int(response) > len(fruits)):
        print('Invalid Response')
        enternum()
    else:
        for reponse in range(len(fruits)):
            out = response + '.' + fruits[int(response) - 1]
        print out


def addfruit2():
    """Enter a user inputted fruit to the beginning of the list with the '+' operator"""
    print ('Enter a fruit to add at the beginning of the list')
    response = input("==> ").strip()
    add_fruit = []
    add_fruit = response
    newfruitslist = add_fruit + fruits
    return newfruitslist

def addfruits3():
    """Add another fruit to the beginning of the list using insert() and display the list."""
    print ('Enter another fruit to add at the beginning of the list')
    response = input("==> ").strip()
    fruits.insert(0,response)
    return fruits


def showpfruits():
    """Display all fruits that begin with P"""
    for i in range(len(fruits)):
        if fruits[i].startswith('P'):
            print (fruits[i])


def removefruit():
    """Remove the last fruit from the list"""
    copy_fruits = fruits[:]
    copy_fruits.pop()
    return copy_fruits


def deletechoosenfruit():
    """Ask the user for a fruit to delete and find it and delete it."""
    print('Enter the fruit to delete from the below list:')
    showfruits(new_fruits)
    response = input("==> ")
    new_fruits.remove(response)
    return new_fruits

def likeafruit():
    """Ask the user for input and perform a set of actions based on whether they like the fruit or not."""
    fruits2 = fruits[:]
    for i in range(len(fruits2)):
        print('Do you like ' + fruits2[i].lower() + '?')
        answers = ['yes','no']
        response = input("==> ").strip()
        while response.lower() not in answers:
            print('Please enter yes or no')
            response = input("==> ").strip()
            print response.lower()
            if response.lower() == 'no':
                fruits2.remove(fruits2[i])
    return fruits2         


if __name__ == "__main__":
    showfruits(fruits)
    
    addfruit()
    showfruits(fruits) #display the list#
    
    enternum()
    
   # addfruit2()
   # showfruits(fruits)
    
    addfruits3() #add a fruit to the beginning of the list using insert()#
    showfruits(fruits) #display the list#
    
    print('Fruits starting with P are:')
    showpfruits()
    
    print('The list of Fruits:')
    showfruits(fruits) #display the list#
    
    print('The list after removing the last fruit:')
    new_fruits =  removefruit()
    showfruits(new_fruits)

    deletechoosenfruit()
    print('The list of fruits after deleting the choosen fruit:')
    showfruits(new_fruits)

    likefruits = likeafruit()
    showfruits(likefruits)
