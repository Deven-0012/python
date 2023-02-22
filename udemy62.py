def user_input():
    choice = 'Deven'
    acceptable_value = range(0,100)
    within_range = False

    while choice.isdigit() == False or within_range == False:

        choice = input("Enter a number between (1-100)")

        if choice.isdigit() == False:
            print('Sorry it is not a digit!')

        if choice.isdigit() == True:
            if int(choice) in acceptable_value:
                within_range = True
            else:
                within_range = False

    return choice
user_input()