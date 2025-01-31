# import time
# for number in range(1, 11):
#     print(number)



# for number in range(60, 0, -1):
#     print(number)
#     time.sleep(0.9)
#     print("KABOOM! WHOOSH! AHHHH! ITS A BOMB!!" )



magic_number = 3405
guess = 0

while guess != magic_number:
    guess=int(input("guess the magic number: "))
    if guess == magic_number:
         print("you got it!")
    elif guess > magic_number :
        print("too high")
    elif guess < magic_number :
        print ("too low")    
    else:
        print("try again!")


print("the while loop is over!")
    