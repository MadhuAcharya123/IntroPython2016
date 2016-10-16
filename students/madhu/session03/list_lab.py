#!/usr/bin/env python3

fruits = ['Apples','Pears','Oranges','Peaches']

def showfruits():
    for i in fruits:
        print (i)        

def addfruit():
    print('Enter another fruit to add to the list:')
    response = input("==> ").strip()
    fruits.append(response) #add the user inputted fruit at the end of the list# 


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


def addfruits3():
    print ('Enter another fruit to add at the beginning of the list')
    response = input("==> ").strip()
    fruits.insert(0,response)


def showpfruits():
    """Display all fruits that begin with P"""
    for i in range(len(fruits)):
        if fruits[i].startswith('P'):
            print (fruits[i])


def removefruit():
    """Remove the last fruit from the list"""
    fruits.pop()


def deletechoosenfruit():
    """Ask the user for a fruit to delete and find it and delete it."""
    print('Enter the fruit to delete from the below list:')
    showfruits()
    response = input("==> ")
    fruits.remove(response)


if __name__ == "__main__":
    showfruits()
    addfruit()
    showfruits() #display the list#
    enternum()
#    addfruit2()
    addfruits3()
    showfruits() #display the list#
    print('Fruits starting with P are:')
    showpfruits()
    print('The list of Fruits:')
    showfruits() #display the list#
    print('The list after removing the last fruit:')
    removefruit()
    showfruits()
    deletechoosenfruit()
    print('The list of fruits after deleting the choosen fruit:')
    showfruits()
