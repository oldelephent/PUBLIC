enter_ammount = int(input("kitne ammount ka % "))
percent = int(input("kitna % "))
full = int(100)

def result():
    result = enter_ammount*percent/full
    print(f"{result}")

result()
