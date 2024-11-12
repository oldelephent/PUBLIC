def calculate_percent():
    while True:
        try:
            enter_ammount = float(input("ammount % "))
            percent = float(input("what % "))
            full = float(100)
            result = round(enter_ammount*percent/full)

            again = input("calc again or type exit:  ")
            if again != '':
                break

        except ValueError:
            print("enter corect value ")
    
calculate_percent()




pyinstaller --icon=ii.ico --onefile .\70.py


