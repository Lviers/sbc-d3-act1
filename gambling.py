from random import randint

num1,num2,num3 = int(input("Enter your first number!!: ")),int(input("Enter your second number!!: ")),int(input("Enter your third number!!: "))
#less lines!!

gamblingaddiction = True


while gamblingaddiction:

    res1,res2,res3 = randint(0,9),randint(0,9),randint(0,9) #less lines


    print("Your swertres number!!: ", num1, num2, num3),  print("Result of the Day!!(?): ", res1, res2, res3) #less lines

    if (num1, num2, num3) == (res1,res2,res3): #less words
        print("You've won !!!")
        gamblingaddiction = False

    elif (num1 == res2,res3) or (num2 == res1,res3) or (num3 == res1,res2,):
    # before = elif (num1 == res1 and  num1 == res3 and  num1 == res3) or (num2 == res1 and  num2 == res2 and  num2  == res3) or (num3 == res1 and  num3 == res2 and  num3  == res3):
        print("You partially win!")
        gamblingaddiction = False

    else:
        print("you lose")
