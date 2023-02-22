game_list = [0,1,2]
def display_gamelist(anyrandomllist):
    print('This is the list ')
    print(anyrandomllist)

def position_choice():
    choice = 'Wrong'
    while choice not in ['0','1','2']:
        choice = input('Enter a index position from (0,1,2)')
        if choice not in ['0','1','2']:
            print('Sorry your input is not in range')
    return int(choice)

def replacement(game_list,position):
    user_placement = input("Enter a sting u want to replace ")

    game_list[position] = user_placement
    return game_list
# result = replacement(game_list,2)
# print(result)

def gamechoice():
    choice = 'Wrong'
    while choice not in ['Y','N']:
        choice = input('Do you want to continue playing Y or N')

        if choice not in ['Y','N']:
            print('Sorry your input is not in range')

        if choice == "Y":
            return True
        else:
            return False
# resuylt = gamechoice()
# print(resuylt)

game_on = True
while game_on:

    display_gamelist(game_list)

    position = position_choice()

    game_list = replacement(game_list,position)

    display_gamelist(game_list)

    game_on = gamechoice()

