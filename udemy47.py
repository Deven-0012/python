from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():

        guess = input("Pick a number btw 0,1 and 2 ")
        return int(guess)

def check_guess(mylist,guess):
    if mylist[guess] == 'o':
        print("Your guess is correct")

    else:
        print("Your guess is incorrect , try again")

# initialize list\
mylist = ['','o','']
# shuffle list
mixedup_list = shuffle_list(mylist)
# user guess
guess = player_guess()
# Check guess
check_guess(mixedup_list,guess)


