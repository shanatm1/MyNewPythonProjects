rows = int(input("how many rows?: "))
columns = int(input("how many columns?: "))
symbol = input("entera symbol to use")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print()