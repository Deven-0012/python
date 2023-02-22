def sq():
    while True:
        try:
            n = int(input('Enter a number '))

        except:
            print("opps an error have occured pls try again  \n")

        else:
            break

    print(n**2)

result = sq()
print(result)