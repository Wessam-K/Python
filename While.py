number = 7

while True:
    user= input("enter y if you would like (Y/n)\n")
    if user == "n":
        break
    usernumb= int(input("guess our "))
    if  usernumb == number:
        print("your number is ok")
    elif abs(number - usernumb) == 1:
        print("you were of by 1 number")
    else:
        print("wrong number")
        
else:
    print("thank you ")


