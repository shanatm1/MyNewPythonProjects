temp = int(input("what is the temperature outside?: "))
if not(temp >= 0 and temp < 30):
    print("its a nice day, go out !!!")
elif temp<0 or temp > 40:
    print("its very bad whether today")
