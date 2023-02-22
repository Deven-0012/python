def check_if_even(num_list):
    evennumber_list = []
    for number in num_list:

        if number % 2 == 0:
            evennumber_list.append(number)
        else:
            pass
    return evennumber_list


result = check_if_even([4,6,8,2])
print(result)