import time
import random
import os
import variacode
import animations

bank_money = 100
casino_money = 0

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


def start(game):
    if game == "casino_game":
        big_text_that_says_casino()
        player_input = input("Start >>>")
        if player_input == "yes" or player_input == "y" or player_input == "Yes":
            place = 0
