from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_in_process = True
while machine_in_process:
    input_choice = input(f"What do you want to drink? Type one the following: {menu.get_items()} --> ")
    if input_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif input_choice == "turn off machine":
        machine_in_process = False
        print("See you next time!")
    else:
        user_choice = menu.find_drink(input_choice)
        if coffee_maker.is_resource_sufficient(user_choice):
            if money_machine.make_payment(user_choice.cost):
                coffee_maker.make_coffee(user_choice)