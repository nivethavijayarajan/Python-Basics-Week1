def addition(x,y):
    return x + y 
def subtraction(x,y):
    return x - y
def multiple(x,y):
    return x * y
def division(x,y):
    return x / y
def Error_detection():
    return "Invalid Option"

while True:
    print()
    choice=int(input("Available options:\n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Exit \nPlease Enter your option:"))
    if choice == 5:
        print("Good Bye")
        break
    elif choice < 5 and choice > 0:
        x = float(input("Enter a X value:"))
        y = float(input("Enter a Y value:"))
        match choice:
            case 1:
                ans = addition(x,y)
                print(ans)
            case 2:
                ans = subtraction(x,y)
                print(ans)
            case 3:
                ans = multiple(x,y)
                print(ans)
            case 4:
                ans = division(x,y)
                print(ans)
    else:
        print(Error_detection())
    

                


