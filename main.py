import time
import random
import os
import variacode
import animations

bank_money = 100
casino_money = 0
chances = 0
chances1 = 0
chances2 = 0

def deposit(type):
    """Makes the user deposit the money
    from his bank account to the casino money account"""
    global bank_money, casino_money
    if type == "money from bank":
        print("How much money would you like to deposit?")
        how_many = int(input(">>> "))
        if how_many <= bank_money:
            casino_money += how_many
            bank_money -= how_many
        else:
            print("You do not have that amount.")
        variacode.sleep(1)
        animations.custom_loading_animation("Depositing", random.randint(1, 10))

def export_money():
    print("How much money would you like to deposit to your bank?")
    how_many = int(input(">>> "))
    if how_many <= bank_money:
        bank_money += how_many
        casino_money -= how_many
    else:
        print("Nah broh you cant bypass this")
    variacode.sleep(1)
    animations.custom_loading_animation("Depositing to bank", random.randint(1, 20))

def big_text_that_says_casino():
    print("CASINO")
    print("A questionable game")
    print("Made in Python")


def start():
    global chances
    global chances1
    global chances2
    big_text_that_says_casino()
    player_input = input("Start >>>")
    game = True
    while game == True:
        if player_input == "yes" or player_input == "y" or player_input == "Yes":
            print("WHERE TO GO NEXT?")
            next = input("house, casino, work ")
            if next == "work":
                print("You already left there")
            if next == "house":
                print("we dont accept there, you left for the milk")
            else:
                chances = random.randint(1, 10)
                chances1 = random.randint(1, 100)
                chances2 = random.randint(1, 1000)
