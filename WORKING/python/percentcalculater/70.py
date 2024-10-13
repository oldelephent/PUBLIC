def calculate_percent():
    while True:
        try:
            enter_ammount = float(input("kitne ammount ka % "))
            percent = float(input("kitna % "))
            full = float(100)
            result = round(enter_ammount*percent/full)

            again = input("calc again or type exit:  ")
            if again != '':
                break

        except ValueError:
            print("enter corect value ")
    
calculate_percent()





