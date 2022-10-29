import sys

shopping_list = []


def shopping_list_print():
    global shopping_list
    item_num = 0
    for x1 in shopping_list:
        item_num = item_num + 1
        print("+"*30)
        print(f"Object Number: {item_num}","\t++")
        print(f"Object name : {x1[0]}","\t++")
        print(f"Brand Name  : {x1[1]}","\t++")
        print(f"Price  : INR {x1[2]}","\t++")
        print(f"count : {x1[3]}  ","\t  \t++")
        print("+"*20)






def shopping_add():
    global shopping_list
    singleton_set = []
    object_inp = input("Enter the type of object you would like to buy: ")
    brand_inp = input("Please enter it's Brand Name: ")
    cost_inp = input("please enter it's MRP in INR: ")
    count_inp = input("Please enter how many pieces you wanna buy: ")
    singleton_set.append(object_inp)
    singleton_set.append(brand_inp)
    singleton_set.append(cost_inp)
    singleton_set.append(count_inp)
    shopping_list.append(singleton_set)
    print("You Just Added an object item with contents: ")
    print(f"{object_inp} {brand_inp} {cost_inp} {count_inp} ")
    print(f"%"*30)

def rem_shopping_list():
    global shopping_list
    rem_item = int(input("Please Enter Object No. to remove it Permanently: "))
    rem_item = rem_item - 1
    if rem_item <= len(shopping_list):
        pop_up = shopping_list.pop(rem_item)
        print("Successfully removed Item with Contents___")
        for a1 in pop_up:
            print(f"{a1}",end=" ")
        print(f"\n******[ Object {pop_up[0]} successfully removed ]*******")
        print("%"*50)
        print(" "*60)
        print(" "*60)
    else:
        print("Invalid Input , try again")

def update_shopping_list():
    global shopping_list
    update_inp = int(input("Please enter Object number to Update it's entries: "))
    singleton_set = []
    object_inp = input("Enter the type of object you would like to buy: ")
    brand_inp = input("Please enter it's Brand Name: ")
    cost_inp = input("please enter it's MRP in INR: ")
    count_inp = input("Please enter how many pieces you wanna buy: ")
    singleton_set.append(object_inp)
    singleton_set.append(brand_inp)
    singleton_set.append(cost_inp)
    singleton_set.append(count_inp)
    update_inp = update_inp - 1
    if update_inp <= len(shopping_list):
        shopping_list[update_inp] = singleton_set
        print(
            f"You just updated previous Object with :\n  [{singleton_set[0]} , {singleton_set[1]} , {singleton_set[2]} , {singleton_set[3]}]")
    else:
        print("Invalid Input")


def main_menu():
    print("**\t"+"#"*30+"\t **")
    print("**\t"+"#"*30+"\t **")
    print("**\t"+"#"*3+" (ULTIMATE SHOPPING LIST)","\t **")
    print("**\t"+"#"*30+"\t **")
    print("**\t"+"#"*30+"\t **"+"\n"+"*"*39+"\n"+"*"*39)
    print("Press a to print  list ")
    print("Press b to add an item to the list ")
    print("Press c to delete an item from the list ")
    print("Press d to replace an item inside the list ")
    print("Press e to exit ")

    option_inp = input("Please choose an option: ")
    option_inp =  option_inp.lower()
    if option_inp == "a":
        print("******[ SHOPPING OBLECTS ]******")
        shopping_list_print()
    elif option_inp == "b":
        shopping_add()
    elif option_inp == "c":
        rem_shopping_list()
    elif option_inp == "d":
        update_shopping_list()
    elif option_inp == "q":
        sys.exit(0)
    else:
        print("Invlid, Input Please try again")



while True:
    main_menu()